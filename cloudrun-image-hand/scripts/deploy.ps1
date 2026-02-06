param (
    [string]$ProjectId = $(gcloud config get-value project),
    [string]$Region = "asia-southeast1"
)

$ServiceName = "image-hand"

Write-Host "Deploying to Project: $ProjectId in Region: $Region" -ForegroundColor Cyan

# Enable APIs
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com --project $ProjectId

# Deploy from source
gcloud run deploy $ServiceName `
  --source . `
  --region $Region `
  --allow-unauthenticated `
  --memory 1Gi `
  --cpu 1 `
  --timeout 300 `
  --project $ProjectId

Write-Host "Deployment complete!" -ForegroundColor Green
