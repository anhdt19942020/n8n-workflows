#!/bin/bash

# Default values
PROJECT_ID=$(gcloud config get-value project)
REGION="asia-southeast1"
SERVICE_NAME="image-hand"

# Overwrite if provided
if [ ! -z "$1" ]; then
  PROJECT_ID=$1
fi

if [ ! -z "$2" ]; then
  REGION=$2
fi

echo "Deploying to Project: $PROJECT_ID in Region: $REGION"

# Enable APIs
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com --project $PROJECT_ID

# Deploy from source
gcloud run deploy $SERVICE_NAME \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --timeout 300 \
  --project $PROJECT_ID

echo "Deployment complete!"
