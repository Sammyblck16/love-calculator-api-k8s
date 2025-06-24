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
