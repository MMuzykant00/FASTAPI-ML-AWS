# 🚀 FastAPI ML API on AWS  

## 📌 Overview  
This project is a **FastAPI-based Machine Learning API** for binary classification. It uses **Docker** for containerization and is deployed on **AWS EC2** for scalability.  

**Tech Stack:** FastAPI | Docker | AWS EC2  

---

## 🚀 Quick Start  



```
### 1 Clone the Repository  
git clone https://github.com/MMuzykant00/fastapi-ml-aws.git
cd fastapi-ml-aws


### 2 Clone the Repository  


docker build -t fastapi-ml-api .
docker run -p 8000:8000 fastapi-ml-api


### 3 Deployment on AWS

ssh -i "fastapi-key.pem" ubuntu@51.20.60.81

git pull origin main
docker build -t fastapi-ml-api .
docker run -d -p 8000:8000 fastapi-ml-api


Live API: http://51.20.60.81:8000/docs


