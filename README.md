# 🧠 End-to-End Machine Learning Project

Welcome to the End-to-End Machine Learning Project repository! This project demonstrates a complete ML workflow—from data preprocessing and model training to containerized deployment on the cloud—using industry-standard tools and best practices. The final model is deployed using **FastAPI**, **Docker**, and **Google Cloud Platform (GCP)**.

---

## 🚀 Project Overview

This repository contains an end-to-end machine learning pipeline that covers the following stages:

- ✅ Data Collection & Preprocessing  
- ✅ Exploratory Data Analysis (EDA)  
- ✅ Feature Engineering  
- ✅ Model Selection & Training  
- ✅ Model Evaluation  
- ✅ Model Deployment (via FastAPI & Docker)  
- ✅ Cloud Deployment (on Google Cloud Platform)

---

## ⚙️ Tech Stack & Libraries

- **Programming Language**: Python 3.x  
- **ML Libraries**: `scikit-learn`, `CatBoost`, `pandas`, `numpy`, `matplotlib`, `seaborn`  
- **Web Framework**: `FastAPI`  
- **Containerization**: Docker  
- **Cloud Platform**: Google Cloud Platform (Cloud Run, Compute Engine)  
- **Version Control**: Git & GitHub  

---

## 📂 Repository Structure

```text
MLproject/
│
├── data/                  # Raw and processed data files
├── notebooks/             # Jupyter notebooks for EDA and experimentation
├── src/                   # Core source code (preprocessing, models, utils)
├── templates/             # HTML templates (if using a web UI)
├── Dockerfile             # Docker build file
├── requirements.txt       # Required Python dependencies
├── app.py                 # FastAPI application entrypoint
├── README.md              # This documentation file
└── ...

```
### 💻 How to Run Locally

#### 1.Clone the repository
```bash
git clone https://github.com/vikranth007/MLproject.git
cd MLproject
```
#### 2.install dependencies
```bash
pip install -r requirements.txt
```
#### 3.Run the FastAPI
```bash
python app.py
```

#### 4.Open your browser and go to http://localhost:5000


### 🐳 Docker Deployment

#### 1.Build the Dcoker image

```bash
docker build -t mlproject-app .
```

#### 2.Run the Docker container

```bash
docker run -p 5000:5000 mlproject-app 
```

###  ☁️ GCP Deployment (Cloud Run)

#### 1.Containerize your app using the Dockerfile (as above).

#### 2.Push the image to Google Container Registry.

```bash
gcloud builds submit --tag gcr.io/[YOUR_PROJECT_ID]/mlproject-app
```
#### 3.Deploy to Cloud Run

```bash
gcloud run deploy --image gcr.io/[YOUR_PROJECT_ID]/mlproject-app --platform managed
```
#### 4.Access Your Web App
After deployment, GCP provides a public URL for your app.




### 🔌 Example API Request

You can send a POST request to the `/predict` endpoint as follows:

```bash
curl -X POST "http://localhost:5000/predict" -H "Content-Type: application/json" -d '{
  "feature1": value,
  "feature2": value,
  "feature3": value
}'
```
You can also visit `/docs` for the Swagger UI interface to test the API interactively.

### ✨ Features & Highlights

- 📊 Full Machine Learning Workflow: From raw data to production deployment

- ☁️ Cloud Ready: Easily deployable on GCP via Docker & Cloud Run

- 🧱 Modular Codebase: Easy to adapt for other datasets or use cases

- 🔄 REST API Support: Predict via Swagger UI or API calls

- 📘 Well-documented: Easy to understand and reproduce

### 📊 Results

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 92.3% |
| Precision | 90.1% |
| Recall    | 91.7% |
| F1 Score  | 90.9% |
| ROC-AUC   | 0.953 |



### 🔮 Future Improvements

- Add input validation and error handling in the API

- Implement CI/CD pipeline for automated deployment

- Extend to multi-model comparison with dashboards

- Add authentication & authorization for secure endpoints























