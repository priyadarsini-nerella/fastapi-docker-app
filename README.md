# fastapi-docker-app
🏡 California Housing ML API (FastAPI + Docker)
📖 Overview
This project demonstrates a machine learning model deployed with FastAPI and Docker, using the California Housing dataset. The API serves predictions on housing prices based on input features, with interactive documentation via Swagger UI.

It showcases skills in:

Data analysis & ML (scikit‑learn)

Backend development (FastAPI)

Containerization (Docker)

Deployment readiness (Render/Cloud)

⚙️ Features
Trained regression model on California Housing dataset

REST API endpoints for predictions

Interactive API docs at /docs

Dockerized for reproducible deployment

🚀 Getting Started
Local Setup
Clone the repository:

bash
git clone https://github.com/priyadarsini-nerella/fastapi-docker-app.git
cd fastapi-docker-app
Install dependencies:

bash
pip install -r requirements.txt
Run locally:

bash
uvicorn main:app --reload
Visit: http://localhost:8000/docs (localhost in Bing)

Docker Setup
Build the image:

bash
docker build -t fastapi-app .
Run the container:

bash
docker run -d -p 8000:8000 fastapi-app
Access the API:

http://localhost:8000

http://localhost:8000/docs (localhost in Bing)
