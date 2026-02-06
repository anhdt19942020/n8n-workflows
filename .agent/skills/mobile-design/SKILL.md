---
name: mobile-design
description: Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Teaches principles, not fixed values. Use when building React Native, Flutter, or native mobile apps.
allowed-tools: Read, Glob, Grep, Bash
---

# Hệ Thống Thiết Kế Mobile

> **Triết Lý:** Ưu tiên cảm ứng (Touch-first). Tiết kiệm pin. Tôn trọng nền tảng. Có khả năng offline.
> **Nguyên Tắc Cốt Lõi:** Mobile KHÔNG PHẢI là desktop thu nhỏ. TƯ DUY theo ràng buộc mobile, HỎI về lựa chọn nền tảng.

---

## 🔧 Runtime Scripts

**Thực thi các script này để xác thực (đừng đọc, chỉ chạy):**

| Script | Mục Đích | Cách Dùng |
|--------|----------|-----------|
| `scripts/mobile_audit.py` | Mobile UX & Touch Audit | `python scripts/mobile_audit.py <project_path>` |

---

## 🔴 BẮT BUỘC: Đọc Các File Tham Khảo Trước Khi Làm Việc!

**⛔ KHÔNG bắt đầu phát triển cho đến khi bạn đọc các file liên quan:**

### Phổ Quát (Luôn Đọc)

| File | Nội Dung | Trạng Thái |
|------|----------|------------|
| **[mobile-design-thinking.md](mobile-design-thinking.md)** | **⚠️ ANTI-MEMORIZATION: Buộc tư duy, ngăn chặn mặc định của AI** | **⬜ QUAN TRỌNG ĐẦU TIÊN** |
| **[touch-psychology.md](touch-psychology.md)** | **Định luật Fitts, cử chỉ, xúc giác (haptics), vùng ngón cái** | **⬜ QUAN TRỌNG** |
| **[mobile-performance.md](mobile-performance.md)** | **Hiệu năng RN/Flutter, 60fps, bộ nhớ** | **⬜ QUAN TRỌNG** |
| **[mobile-backend.md](mobile-backend.md)** | **Push notifications, đồng bộ offline, mobile API** | **⬜ QUAN TRỌNG** |
| **[mobile-testing.md](mobile-testing.md)** | **Tháp kiểm thử, E2E, đặc thù nền tảng** | **⬜ QUAN TRỌNG** |
| **[mobile-debugging.md](mobile-debugging.md)** | **Native vs JS debugging, Flipper, Logcat** | **⬜ QUAN TRỌNG** |
| [mobile-navigation.md](mobile-navigation.md) | Tab/Stack/Drawer, deep linking | ⬜ Đọc |
| [mobile-typography.md](mobile-typography.md) | System fonts, Dynamic Type, a11y | ⬜ Đọc |
| [mobile-color-system.md](mobile-color-system.md) | OLED, chế độ tối, nhận thức về pin | ⬜ Đọc |
| [decision-trees.md](decision-trees.md) | Chọn Framework/state/storage | ⬜ Đọc |

> 🧠 **mobile-design-thinking.md là ƯU TIÊN!** File này đảm bảo AI tư duy thay vì dùng các pattern học thuộc lòng.

### Đặc Thù Nền Tảng (Đọc Dựa Trên Mục Tiêu)

| Nền Tảng | File | Nội Dung | Khi Nào Đọc |
|----------|------|----------|-------------|
| **iOS** | [platform-ios.md](platform-ios.md) | Human Interface Guidelines, SF Pro, SwiftUI patterns | Xây dựng cho iPhone/iPad |
| **Android** | [platform-android.md](platform-android.md) | Material Design 3, Roboto, Compose patterns | Xây dựng cho Android |
| **Đa Nền Tảng** | Cả hai ở trên | Các điểm phân nhánh nền tảng | React Native / Flutter |

> 🔴 **Nếu xây dựng cho iOS → Đọc platform-ios.md TRƯỚC!**
> 🔴 **Nếu xây dựng cho Android → Đọc platform-android.md TRƯỚC!**
> 🔴 **Nếu đa nền tảng → Đọc CẢ HAI và áp dụng logic nền tảng có điều kiện!**

---

## ⚠️ QUAN TRỌNG: HỎI TRƯỚC KHI GIẢ ĐỊNH (BẮT BUỘC)

> **DỪNG LẠI! Nếu yêu cầu của người dùng là mở, ĐỪNG mặc định dùng sở thích của bạn.**

### Bạn PHẢI Hỏi Nếu Không Được Chỉ Định:

| Khía Cạnh | Hỏi | Tại Sao |
|-----------|-----|---------|
| **Nền tảng** | "iOS, Android, hay cả hai?" | Ảnh hưởng MỌI quyết định thiết kế |
| **Framework** | "React Native, Flutter, hay native?" | Quyết định pattern và công cụ |
| **Điều hướng** | "Tab bar, drawer, hay stack-based?" | Quyết định UX cốt lõi |
| **Trạng thái** | "Quản lý state thế nào? (Zustand/Redux/Riverpod/BLoC?)" | Nền tảng kiến trúc |
| **Offline** | "Cái này có cần hoạt động offline không?" | Ảnh hưởng chiến lược dữ liệu |
| **Thiết bị mục tiêu** | "Chỉ điện thoại, hay hỗ trợ tablet?" | Độ phức tạp bố cục |

### ⛔ CÁC ANTI-PATTERNS MOBILE CỦA AI (DANH SÁCH CẤM)

> 🚫 **Đây là các xu hướng mặc định của AI mà PHẢI tránh!**

#### Các Tội Lỗi Về Hiệu Năng

| ❌ ĐỪNG BAO GIỜ | Tại Sao Sai | ✅ LUÔN LÀM |
|-----------------|-------------|-------------|
| **ScrollView cho danh sách dài** | Render TẤT CẢ item, bùng nổ bộ nhớ | Dùng `FlatList` / `FlashList` / `ListView.builder` |
| **Hàm renderItem inline** | Hàm mới mỗi lần render, tất cả item re-render | `useCallback` + `React.memo` |
| **Thiếu keyExtractor** | Key dựa trên index gây bug khi sắp xếp lại | ID duy nhất, ổn định từ dữ liệu |
| **Bỏ qua getItemLayout** | Layout bất đồng bộ = janky scroll | Cung cấp khi item có chiều cao cố định |
| **setState() khắp nơi** | Rebuild widget không cần thiết | State khoanh vùng, `const` constructors |
| **Native driver: false** | Animation bị chặn bởi JS thread | `useNativeDriver: true` luôn luôn |
| **console.log trong production** | Chặn JS thread nghiêm trọng | Xóa trước khi build release |
| **Bỏ qua React.memo/const** | Mọi item re-render khi có thay đổi | Memoize list items LUÔN LUÔN |

#### Các Tội Lỗi Về Cảm Ứng/UX

| ❌ ĐỪNG BAO GIỜ | Tại Sao Sai | ✅ LUÔN LÀM |
|-----------------|-------------|-------------|
| **Vùng chạm < 44px** | Không thể tap chính xác, gây ức chế | Tối thiểu 44pt (iOS) / 48dp (Android) |
| **Khoảng cách < 8px giữa các mục tiêu** | Tap nhầm vào bên cạnh | Khoảng cách tối thiểu 8-12px |
| **Tương tác chỉ dùng cử chỉ** | Người khiếm khuyết vận động bị loại bỏ | Luôn cung cấp nút bấm thay thế |
| **Không có trạng thái loading** | Người dùng tưởng app bị treo | LUÔN hiển thị phản hồi đang tải |
| **Không có trạng thái lỗi** | Người dùng bị kẹt, không lối thoát | Hiển thị lỗi với tùy chọn thử lại |
| **Không xử lý offline** | Crash/chặn khi mất mạng | Xuống cấp nhẹ nhàng (Graceful degradation), data cached |
| **Phớt lờ quy ước nền tảng** | Người dùng bối rối, phá vỡ trí nhớ cơ bắp | iOS cảm giác như iOS, Android cảm giác như Android |

#### Các Tội Lỗi Về Bảo Mật

| ❌ ĐỪNG BAO GIỜ | Tại Sao Sai | ✅ LUÔN LÀM |
|-----------------|-------------|-------------|
| **Token trong AsyncStorage** | Dễ truy cập, bị trộm trên thiết bị root | `SecureStore` / `Keychain` / `EncryptedSharedPreferences` |
| **Hardcode API keys** | Dịch ngược từ APK/IPA | Biến môi trường, lưu trữ bảo mật |
| **Bỏ qua SSL pinning** | Có thể bị tấn công MITM | Pin chứng chỉ trong production |
| **Log dữ liệu nhạy cảm** | Log có thể bị trích xuất | Không bao giờ log token, mật khẩu, PII |

#### Các Tội Lỗi Về Kiến Trúc

| ❌ ĐỪNG BAO GIỜ | Tại Sao Sai | ✅ LUÔN LÀM |
|-----------------|-------------|-------------|
| **Logic nghiệp vụ trong UI** | Không test được, không bảo trì được | Tách biệt lớp Service |
| **Global state cho mọi thứ** | Re-render không cần thiết, phức tạp | Local state là mặc định, lift lên khi cần |
| **Deep linking là ý nghĩ sau cùng** | Thông báo, chia sẻ bị hỏng | Lên kế hoạch deep links từ ngày đầu |
| **Bỏ qua dispose/cleanup** | Rò rỉ bộ nhớ, zombie listeners | Dọn dẹp subscriptions, timers |

---

## 📱 Ma Trận Quyết Định Nền Tảng

### Khi Nào Thống Nhất vs Phân Nhánh

```
                    THỐNG NHẤT (giống nhau cả 2)  PHÂN NHÁNH (đặc thù nền tảng)
                    ────────────────────────────  ─────────────────────────────
Business Logic      ✅ Luôn luôn                  -
Data Layer          ✅ Luôn luôn                  -
Core Features       ✅ Luôn luôn                  -
                    
Navigation          -                             ✅ iOS: vuốt cạnh, Android: nút back
Gestures            -                             ✅ Cảm giác native của nền tảng
Icons               -                             ✅ SF Symbols vs Material Icons
Date Pickers        -                             ✅ Native pickers cảm giác đúng hơn
Modals/Sheets       -                             ✅ iOS: bottom sheet vs Android: dialog
Typography          -                             ✅ SF Pro vs Roboto (hoặc custom)
Error Dialogs       -                             ✅ Quy ước nền tảng cho alerts
```

### Tham Khảo Nhanh: Mặc Định Nền Tảng

| Thành Phần | iOS | Android |
|------------|-----|---------|
| **Font Chính** | SF Pro / SF Compact | Roboto |
| **Vùng Chạm Tối Thiểu** | 44pt × 44pt | 48dp × 48dp |
| **Điều Hướng Quay Lại** | Vuốt cạnh trái | Nút back hệ thống/cử chỉ |
| **Icon Tab Dưới** | SF Symbols | Material Symbols |
| **Action Sheet** | UIActionSheet từ dưới lên | Bottom Sheet / Dialog |
| **Tiến Trình** | Spinner | Linear progress (Material) |
| **Kéo Để Tải Lại** | Native UIRefreshControl | SwipeRefreshLayout |

---

## 🧠 Tâm Lý Học UX Mobile (Tham Khảo Nhanh)

### Định Luật Fitts Cho Cảm Ứng

```
Desktop: Con trỏ chính xác (1px)
Mobile:  Ngón tay không chính xác (~7mm diện tích tiếp xúc)

→ Vùng chạm PHẢI tối thiểu 44-48px
→ Các hành động quan trọng ở VÙNG NGÓN CÁI (dưới màn hình)
→ Các hành động phá hủy XA KHỎI tầm với dễ dàng
```

### Vùng Ngón Cái (Sử Dụng Một Tay)

```
┌─────────────────────────────┐
│      KHÓ VỚI TỚI            │ ← Điều hướng, menu, back
│        (cố vươn)            │
├─────────────────────────────┤
│      VỪA TẦM VỚI            │ ← Hành động phụ
│       (tự nhiên)            │
├─────────────────────────────┤
│      DỄ VỚI TỚI             │ ← PRIMARY CTAs, tab bar
│  (vòng cung tự nhiên ngón cái) │ ← Tương tác nội dung chính
└─────────────────────────────┘
        [  HOME  ]
```

### Cognitive Load (Tải Nhận Thức) Đặc Thù Mobile

| Desktop | Khác Biệt Mobile |
|---------|------------------|
| Nhiều cửa sổ | MỘT tác vụ tại một thời điểm |
| Phím tắt | Cử chỉ chạm |
| Trạng thái Hover | KHÔNG hover (tap hoặc không gì cả) |
| Viewport lớn | Không gian hạn chế, cuộn dọc |
| Chú ý ổn định | Bị gián đoạn liên tục |

Chi tiết đào sâu: [touch-psychology.md](touch-psychology.md)

---

## ⚡ Các Nguyên Tắc Hiệu Năng (Tham Khảo Nhanh)

### Quy Tắc React Native Cốt Tử

```typescript
// ✅ ĐÚNG: Memoized renderItem + React.memo wrapper
const ListItem = React.memo(({ item }: { item: Item }) => (
  <View style={styles.item}>
    <Text>{item.title}</Text>
  </View>
));

const renderItem = useCallback(
  ({ item }: { item: Item }) => <ListItem item={item} />,
  []
);

// ✅ ĐÚNG: FlatList với tất cả tối ưu hóa
<FlatList
  data={items}
  renderItem={renderItem}
  keyExtractor={(item) => item.id}  // Stable ID, KHÔNG PHẢI index
  getItemLayout={(data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  })}
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  windowSize={5}
/>
```

### Quy Tắc Flutter Cốt Tử

```dart
// ✅ ĐÚNG: const constructors ngăn chặn rebuilds
class MyWidget extends StatelessWidget {
  const MyWidget({super.key}); // CONST!

  @override
  Widget build(BuildContext context) {
    return const Column( // CONST!
      children: [
        Text('Static content'),
        MyConstantWidget(),
      ],
    );
  }
}

// ✅ ĐÚNG: Targeted state với ValueListenableBuilder
ValueListenableBuilder<int>(
  valueListenable: counter,
  builder: (context, value, child) => Text('$value'),
  child: const ExpensiveWidget(), // Sẽ không rebuild!
)
```

### Hiệu Năng Animation

```
Tăng tốc GPU (NHANH):       CPU-bound (CHẬM):
├── transform               ├── width, height
├── opacity                 ├── top, left, right, bottom
└── (CHỈ dùng những cái này) ├── margin, padding
                            └── (TRÁNH animate cái này)
```

Hướng dẫn đầy đủ: [mobile-performance.md](mobile-performance.md)

---

## 📝 CHECKPOINT (BẮT BUỘC Trước Bất Kỳ Việc Mobile Nào)

> **Trước khi viết BẤT KỲ code mobile nào, bạn PHẢI hoàn thành checkpoint này:**

```
🧠 CHECKPOINT:

Platform:   [ iOS / Android / Cả Hai ]
Framework:  [ React Native / Flutter / SwiftUI / Kotlin ]
Files Read: [ Liệt kê các file skill bạn đã đọc ]

3 Principles Tôi Sẽ Áp Dụng:
1. _______________
2. _______________
3. _______________

Anti-Patterns Tôi Sẽ Tránh:
1. _______________
2. _______________
```

**Ví dụ:**
```
🧠 CHECKPOINT:

Platform:   iOS + Android (Cross-platform)
Framework:  React Native + Expo
Files Read: touch-psychology.md, mobile-performance.md, platform-ios.md, platform-android.md

3 Principles Tôi Sẽ Áp Dụng:
1. FlatList với React.memo + useCallback cho tất cả danh sách
2. Vùng chạm 48px, vùng ngón cái cho CTA chính
3. Điều hướng đặc thù nền tảng (vuốt cạnh iOS, nút back Android)

Anti-Patterns Tôi Sẽ Tránh:
1. ScrollView cho danh sách → FlatList
2. Inline renderItem → Memoized
3. AsyncStorage cho token → SecureStore
```

> 🔴 **Không điền được checkpoint? → QUAY LẠI VÀ ĐỌC CÁC FILE SKILL.**

---

## 🔧 Cây Quyết Định Framework

```
BẠN ĐANG XÂY DỰNG CÁI GÌ?
        │
        ├── Cần cập nhật OTA + vòng lặp nhanh + team web
        │   └── ✅ React Native + Expo
        │
        ├── Cần UI tùy chỉnh pixel-perfect + hiệu năng cực cao
        │   └── ✅ Flutter
        │
        ├── Tính năng native sâu + tập trung một nền tảng
        │   ├── Chỉ iOS → SwiftUI
        │   └── Chỉ Android → Kotlin + Jetpack Compose
        │
        ├── Codebase RN hiện tại + tính năng mới
        │   └── ✅ React Native (bare workflow)
        │
        └── Doanh nghiệp + codebase Flutter hiện tại
            └── ✅ Flutter
```

Cây quyết định đầy đủ: [decision-trees.md](decision-trees.md)

---

## 📋 Checklist Trước Khi Phát Triển

### Trước Khi Bắt Đầu BẤT KỲ Dự Án Mobile Nào

- [ ] **Đã xác nhận nền tảng?** (iOS / Android / Cả Hai)
- [ ] **Đã chọn Framework?** (RN / Flutter / Native)
- [ ] **Đã quyết định pattern điều hướng?** (Tabs / Stack / Drawer)
- [ ] **Đã chọn quản lý state?** (Zustand / Redux / Riverpod / BLoC)
- [ ] **Đã biết yêu cầu offline?**
- [ ] **Đã lên kế hoạch deep linking từ ngày đầu?**
- [ ] **Đã xác định thiết bị mục tiêu?** (Phone / Tablet / Cả Hai)

### Trước Mỗi Màn Hình

- [ ] **Vùng chạm ≥ 44-48px?**
- [ ] **CTA chính trong vùng ngón cái?**
- [ ] **Có trạng thái Loading?**
- [ ] **Có trạng thái Lỗi với retry?**
- [ ] **Đã cân nhắc xử lý Offline?**
- [ ] **Đã tuân thủ quy ước nền tảng?**

### Trước Khi Release

- [ ] **Đã xóa console.log?**
- [ ] **Dùng SecureStore cho dữ liệu nhạy cảm?**
- [ ] **Đã bật SSL pinning?**
- [ ] **Danh sách đã tối ưu (memo, keyExtractor)?**
- [ ] **Dọn dẹp bộ nhớ khi unmount?**
- [ ] **Đã test trên thiết bị cấu hình thấp?**
- [ ] **Nhãn Accessibility trên mọi phần tử tương tác?**

---

## 📚 Các File Tham Khảo

Để hướng dẫn sâu hơn về các lĩnh vực cụ thể:

| File | Khi Nào Dùng |
|------|--------------|
| [mobile-design-thinking.md](mobile-design-thinking.md) | **ĐẦU TIÊN! Chống học vẹt, buộc tư duy theo ngữ cảnh** |
| [touch-psychology.md](touch-psychology.md) | Hiểu tương tác chạm, ĐL Fitts, thiết kế cử chỉ |
| [mobile-performance.md](mobile-performance.md) | Tối ưu RN/Flutter, 60fps, bộ nhớ/pin |
| [platform-ios.md](platform-ios.md) | Thiết kế đặc thù iOS, tuân thủ HIG |
| [platform-android.md](platform-android.md) | Thiết kế đặc thù Android, Material Design 3 |
| [mobile-navigation.md](mobile-navigation.md) | Các pattern điều hướng, deep linking |
| [mobile-typography.md](mobile-typography.md) | Tỷ lệ chữ, font hệ thống, khả năng truy cập |
| [mobile-color-system.md](mobile-color-system.md) | Tối ưu OLED, chế độ tối, pin |
| [decision-trees.md](decision-trees.md) | Quyết định framework, state, storage |

---

> **Ghi nhớ:** Người dùng mobile thiếu kiên nhẫn, hay bị gián đoạn, và dùng ngón tay không chính xác trên màn hình nhỏ. Hãy thiết kế cho điều kiện TỆ NHẤT: mạng kém, một tay, nắng gắt, pin yếu. Nếu nó hoạt động tốt ở đó, nó sẽ hoạt động tốt ở mọi nơi.
