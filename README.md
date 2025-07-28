# End-to-End Machine Learning Project
Welcome to the End-to-End Machine Learning Project repository! This project demonstrates the complete ML workflow—from data processing and model building to deployment—using modern, industry-standard tools. The project is deployed on Google Cloud Platform (GCP) for real-world accessibility and scalability.

## 🚀 Project Overview

This repository contains an end-to-end machine learning solution that covers the following steps:

 - Data Collection & Preprocessing

- Exploratory Data Analysis (EDA)

- Feature Engineering

- Model Selection & Training

- Model Evaluation

- Model Deployment (via Flask API & Docker)

- Cloud Deployment (on Google Cloud Platform)

## ⚙️ Tech Stack & Libraries

- Programming Languages: Python 3.x

- ML Libraries: scikit-learn, CatBoost, pandas, numpy, matplotlib, seaborn

- Web Framework: FastAPI

- Containerization: Docker

- Cloud Platform: Google Cloud Platform (Cloud Run, Compute Engine, etc.)

- Version Control: Git & GitHub


## 📂 Repository Structure

```TEXT 
MLproject/
│
├── data/                  # Data files (input, output, processed)
├── notebooks/             # Jupyter Notebooks for EDA & prototyping
├── src/                   # Core source code: preprocessing, models, utils
├── templates/             # HTML templates for Flask app (if applicable)
├── Dockerfile             # For containerization
├── requirements.txt       # Python dependencies
├── app.py                 # FastAPI application entrypoint
├── README.md              # Project documentation
└── ...
```
### 🏗 How to Run Locally

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
#### 4.After deployment, GCP provides a public URL for your app.


### ✨ Features & Highlights

- End-to-End Workflow: From raw data to deployed Web API.

- Cloud Ready: Easily deployable on Google Cloud Platform.

- Reusable Modular Codebase: Easy to adapt for new datasets or problems.

- Interactive API: Predict using a REST API or simple web form.

- Comprehensive Documentation: Explains every step and how to reproduce results.

### 📊 Results:

Metric	Value

- Accuracy	92.3%

- Precision	90.1%

- Recall	91.7%

- F1 Score	90.9%

- ROC-AUC	0.953













