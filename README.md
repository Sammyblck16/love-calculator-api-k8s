# 💖 Love Calculator API (Kubernetes Deployment)

This project is a fun and simple REST API that calculates a "love score" between two names. It's built with Python and Flask, containerized with Docker, and ready to deploy on Kubernetes.

---

## 🚀 Features

- Accepts two names via POST request
- Calculates a love score based on letter counts
- Returns a fun message along with the score
- Exposes an HTTP API via `/calculate`
- Includes Kubernetes manifests for deployment

---

## 📦 API Usage

### Endpoint

```http
POST /calculate
Content-Type: application/json

.
├── app.py               # Flask web server
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image configuration
├── deployment.yaml      # Kubernetes Deployment
├── service.yaml         # Kubernetes Service (NodePort)
└── README.md            # Project documentation


---

## ✅ 2. `.gitignore`

This prevents unnecessary files from being pushed:

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.env.*
*.sqlite3
*.log
*.DS_Store
.vscode/
.idea/
*.swp

1. docker-push.sh — Bash Script to Build & Push to Docker Hub
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

Usage
Save it as docker-push.sh

Make it executable:

bash

chmod +x docker-push.sh

./docker-push.sh

2. .github/workflows/docker-image.yml — GitHub Actions CI
This workflow automatically builds and pushes your Docker image when you push to main.

📄 File: .github/workflows/docker-image.yml

name: Build and Push Docker image

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: your-dockerhub-username/love-calculator:latest

GitHub Secrets Setup
To use this GitHub Actions workflow, go to your repository:

Navigate to Settings → Secrets and variables → Actions

Add the following Repository Secrets:

DOCKER_USERNAME

DOCKER_PASSWORD (your Docker Hub password or access token)

