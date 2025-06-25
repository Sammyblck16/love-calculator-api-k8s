# 💖 Love Calculator API (Kubernetes Deployment)

This project is built with **Python** and **Flask**, containerized using **Docker**, and ready to deploy on **Kubernetes**.

---

## 🚀 Features

- Accepts two names via POST request
- Calculates a love score based on letter counts
- Returns a fun message along with the score
- Exposes an HTTP API via `/calculate`
- Includes Kubernetes manifests for deployment

---

## 📦 API Usage

### ▶️ Endpoint

```
POST /calculate
Content-Type: application/json
```

### 🧪 Example Request

```json
{
  "name1": "Alice",
  "name2": "Bob"
}
```

### ✅ Example Response

```json
{
  "score": 74,
  "message": "Your score is 74."
}
```

---

## 📁 Project Structure

```
.
├── app.py               # Flask web server
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image configuration
├── deployment.yaml      # Kubernetes Deployment
├── service.yaml         # Kubernetes Service (NodePort)
├── docker-push.sh       # Script to push Docker image
├── .gitignore           # Ignore unnecessary files
└── README.md            # Project documentation
```

---

## 🐳 Docker Push Script

Save the script below as `docker-push.sh`:

```bash
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
```

### 📦 Usage

```bash
chmod +x docker-push.sh
./docker-push.sh
```

---

## ☸️ GitHub Actions CI

Create a GitHub Actions workflow file at `.github/workflows/docker-image.yml`:

```yaml
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
```

### 🔐 GitHub Secrets Setup

To use this GitHub Actions workflow:

1. Navigate to **Settings → Secrets and variables → Actions**
2. Add the following **Repository Secrets**:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD` (your Docker Hub password or access token)

---

## 📄 .gitignore

This prevents unnecessary or sensitive files from being pushed:

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
```

---

## 📜 License

This project is open source under the [MIT License](LICENSE).
