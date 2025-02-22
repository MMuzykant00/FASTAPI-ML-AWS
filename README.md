# 🚀 FastAPI Machine Learning API on AWS

## 📌 Overview  
This project is a **FastAPI-based Machine Learning API** for binary classification. It is deployed on **AWS EC2** using **Docker** for scalability and ease of deployment.

The **Random Forest model** was selected as the final model because it outperformed XGBoost in terms of efficiency and simplicity in implementation.

---

## 🎯 Features  
✔ **ML Model Deployment**: Uses **Random Forest** for binary classification.  
✔ **FastAPI for API Development**: Provides a clean REST API for making predictions.  
✔ **Swagger UI**: Easily test API endpoints at **[http://51.20.60.81:8000/docs](http://51.20.60.81:8000/docs)**.  
✔ **Dockerized Deployment**: Containerized for easy scalability and cloud deployment.  
✔ **AWS EC2 Hosting**: Runs on an AWS EC2 instance with secured SSH access.  

---

## 📂 Project Structure  
```bash
fastapi-ml-aws/
│── app/                # FastAPI application code
│── model/              # Trained ML models (Random Forest, XGBoost)
│── data/               # Sample datasets for testing
│── Dockerfile          # Docker configuration for deployment
│── requirements.txt    # Python dependencies
│── main.py             # API entry point
│── README.md           # Documentation
│── .gitignore          # Excluded files (e.g., __pycache__, sensitive keys)

# 🚀 Getting Started

### 1.Clone the Repository

git clone https://github.com/MMuzykant00/fastapi-ml-aws.git
cd fastapi-ml-aws
### 2.Set Up a Virtual Environment (Optional but Recommended)


### 3.Install Dependencies

pip install -r requirements.txt

### 4. Run FastAPI Locally

uvicorn main:app --reload

### 5.Build and Run the Docker Container

docker build -t fastapi-ml-api .
docker run -p 8000:8000 fastapi-ml-api


#🚀  Deployment on AWS


ssh -i "fastapi-key.pem" ubuntu@51.20.60.81

git pull origin main


docker build -t fastapi-ml-api .
docker run -d -p 8000:8000 fastapi-ml-api


Visit: http://51.20.60.81:8000/docs













