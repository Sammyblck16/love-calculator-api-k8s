#!/bin/bash

# -------- CONFIGURE THIS --------
DOCKER_USERNAME="your-dockerhub-username"
IMAGE_NAME="love-calculator"
TAG="latest"
# --------------------------------

echo "🚀 Building Docker image..."
docker build -t $DOCKER_USERNAME/$IMAGE_NAME:$TAG .

echo "🔐 Logging in to Docker Hub..."
docker login

echo "📤 Pushing Docker image to Docker Hub..."
docker push $DOCKER_USERNAME/$IMAGE_NAME:$TAG

echo "✅ Done! Image pushed as $DOCKER_USERNAME/$IMAGE_NAME:$TAG"

