# 🚀 FastAPI Machine Learning API on AWS

## 📌 Overview
This project is a **FastAPI-based Machine Learning API** for binary classification. It is deployed on **AWS EC2** using **Docker** for scalability and ease of deployment.

The **Random Forest model** was selected as the final model because it outperformed XGBoost in terms of efficiency and simplicity in implementation.

## 🏗️ Features
- ✅ **ML Model Deployment**: Uses **Random Forest** for binary classification.
- ✅ **FastAPI for API Development**: Provides a clean REST API for making predictions.
- ✅ **Swagger UI**: Easily test API endpoints at [`http://51.20.60.81:8000/docs`](http://51.20.60.81:8000/docs).
- ✅ **Dockerized Deployment**: Containerized for easy scalability and cloud deployment.
- ✅ **AWS EC2 Hosting**: Runs on an AWS EC2 instance with secured SSH access.

## 📂 Project Structure



## 🚀 Getting Started

### 🔹 1️⃣ Clone the Repository
```bash
git clone https://github.com/MMuzykant00/fastapi-ml-aws.git
cd fastapi-ml-aws

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

pip install -r requirements.txt

uvicorn main:app --reload

docker build -t fastapi-ml-api .
docker run -p 8000:8000 fastapi-ml-api

ssh -i "fastapi-key.pem" ubuntu@51.20.60.81

git pull origin main

docker build -t fastapi-ml-api .
docker run -d -p 8000:8000 fastapi-ml-api

Visit: http://51.20.60.81:8000/docs

The Random Forest model was trained and compared with XGBoost, SVM, and Logistic Regression. The evaluation results showed that:

Random Forest had the best balance of performance and efficiency
XGBoost was slightly better but required more computational power
