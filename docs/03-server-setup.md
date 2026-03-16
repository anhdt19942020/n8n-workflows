# 3. Hướng dẫn Setup Server

## Yêu cầu phần cứng

| Quy mô | VPS | RAM | CPU | Disk | Nhà cung cấp gợi ý |
|---------|-----|-----|-----|------|---------------------|
| **Dev/Test** | Local | - | - | - | Máy cá nhân |
| **1-20 khách** | 1 VPS | 2GB | 2 vCPU | 40GB SSD | Contabo, Vultr, DigitalOcean |
| **20-100 khách** | 1 VPS | 4GB | 4 vCPU | 80GB SSD | Contabo, Vultr |
| **100+ khách** | 2+ VPS | 8GB+ | 4+ vCPU | 160GB+ | AWS, GCP |

## Chạy local (Development)

### Yêu cầu
- Node.js >= 22.16 (dùng nvm để quản lý version)

### Lệnh
```bash
# Cài Node.js 22
nvm install 22
nvm use 22

# Chạy n8n
npx -y n8n@latest

# Mở browser: http://localhost:5678
```

### Lưu ý
- n8n mặc định dùng SQLite, data lưu tại `~/.n8n/`
- Lần đầu chạy cần tạo account owner

## Chạy Production (Docker trên VPS)

### Bước 1: Cài Docker

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Cài Docker Compose
sudo apt install docker-compose-plugin
```

### Bước 2: Tạo thư mục dự án

```bash
mkdir -p /opt/n8n
cd /opt/n8n
```

### Bước 3: Tạo docker-compose.yml

```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    environment:
      # Database
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=n8n
      - DB_POSTGRESDB_USER=n8n
      - DB_POSTGRESDB_PASSWORD=${DB_PASSWORD}
      # Domain & SSL
      - N8N_HOST=${DOMAIN}
      - N8N_PROTOCOL=https
      - N8N_PORT=5678
      - WEBHOOK_URL=https://${DOMAIN}/
      # Timezone
      - GENERIC_TIMEZONE=Asia/Ho_Chi_Minh
      - TZ=Asia/Ho_Chi_Minh
      # Security
      - N8N_ENCRYPTION_KEY=${ENCRYPTION_KEY}
    volumes:
      - n8n_data:/home/node/.n8n
    depends_on:
      postgres:
        condition: service_healthy

  postgres:
    image: postgres:16-alpine
    restart: always
    environment:
      - POSTGRES_USER=n8n
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=n8n
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U n8n"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  n8n_data:
  postgres_data:
```

### Bước 4: Tạo file .env

```bash
cat > .env << 'EOF'
DOMAIN=n8n.yourdomain.com
DB_PASSWORD=your_strong_password_here
ENCRYPTION_KEY=your_random_encryption_key_here
EOF
```

Tạo encryption key:
```bash
openssl rand -hex 32
```

### Bước 5: Setup Nginx + SSL

```bash
sudo apt install nginx certbot python3-certbot-nginx
```

Tạo file nginx config:
```nginx
# /etc/nginx/sites-available/n8n
server {
    listen 80;
    server_name n8n.yourdomain.com;

    location / {
        proxy_pass http://localhost:5678;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        chunked_transfer_encoding off;
        proxy_buffering off;
        proxy_cache off;
    }
}
```

Kích hoạt + SSL:
```bash
sudo ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
sudo certbot --nginx -d n8n.yourdomain.com
```

### Bước 6: Khởi động

```bash
cd /opt/n8n
docker compose up -d

# Xem logs
docker compose logs -f n8n

# Kiểm tra trạng thái
docker compose ps
```

### Bước 7: Import workflow

Mở `https://n8n.yourdomain.com` → Setup account → Import workflow từ file JSON.

## Backup & Restore

### Backup tự động (cron)

```bash
# Tạo script backup
cat > /opt/n8n/backup.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/opt/n8n/backups"
DATE=$(date +%Y%m%d_%H%M)
mkdir -p $BACKUP_DIR

# Backup PostgreSQL
docker compose exec -T postgres pg_dump -U n8n n8n > $BACKUP_DIR/n8n_db_$DATE.sql

# Backup n8n data
docker compose exec -T n8n tar czf - /home/node/.n8n > $BACKUP_DIR/n8n_data_$DATE.tar.gz

# Xóa backup cũ hơn 30 ngày
find $BACKUP_DIR -mtime +30 -delete

echo "Backup completed: $DATE"
EOF

chmod +x /opt/n8n/backup.sh

# Chạy backup hàng ngày lúc 3h sáng
echo "0 3 * * * /opt/n8n/backup.sh" | crontab -
```

### Restore

```bash
# Restore database
docker compose exec -T postgres psql -U n8n n8n < backups/n8n_db_YYYYMMDD.sql
```

## Monitoring

```bash
# Kiểm tra n8n đang chạy
docker compose ps

# Xem logs realtime
docker compose logs -f n8n --tail 100

# Restart nếu cần
docker compose restart n8n

# Update n8n version
docker compose pull
docker compose up -d
```
