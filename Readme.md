# 🛡️ Insurance Premium Prediction

### Intelligent Machine Learning System for Insurance Premium Category Prediction

A full-stack machine learning application that predicts an insurance premium category based on user information such as BMI, age, lifestyle risk, city tier, income, and occupation.

This project combines a **React frontend**, **FastAPI backend**, and a trained **Machine Learning model** to provide a clean, responsive, and user-friendly prediction experience.

---

## 📖 Overview

Insurance pricing can depend on multiple factors such as age, BMI, lifestyle habits, income level, location, and occupation.

This application uses a machine learning model to analyze these factors and predict the expected insurance premium category.

The system provides an interactive web interface where users can enter their information and receive a machine learning-based prediction.

---

## ✨ Key Features

- 🧠 Machine Learning based insurance premium prediction
- 📊 Automatic BMI calculation
- 👤 Age, weight, height, income and lifestyle inputs
- 🚬 Smoking status analysis
- 🏙️ City-based information
- 💼 Occupation-based prediction
- 🎯 Prediction confidence score
- ⚡ FastAPI REST API
- ⚛️ React frontend
- 📡 Axios API integration
- 📱 Responsive user interface
- 🔄 Real-time frontend and backend communication
- 🌐 Vercel frontend deployment
- ☁️ Render backend deployment
- 📚 FastAPI Swagger API documentation

---

## 🛠️ Tech Stack

### Frontend

- React
- JavaScript
- Vite
- Axios
- HTML5
- CSS3

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- CORS Middleware

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle / Joblib

### Deployment & Tools

- Git
- GitHub
- Vercel
- Render

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      User Input      │
                    │ Age, BMI, Income etc │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    React Frontend    │
                    │      Vite + UI       │
                    └──────────┬───────────┘
                               │
                         HTTP POST Request
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │      /predict        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Feature Processing │
                    │ BMI / Risk / Features│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Machine Learning   │
                    │        Model         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prediction Response  │
                    │ Category + Confidence│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Prediction Card    │
                    │   React Frontend     │
                    └──────────────────────┘
📁 Project Structure
Insurance-premium-Prediction/
│
├── Schema/
│   ├── user_input.py
│   └── prediction_response.py
│
├── model/
│   ├── predict.py
│   └── trained model files
│
├── config/
│
├── insurance-frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── Footer.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Loader.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── PredictionCard.jsx
│   │   │   └── PredictionForm.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── app.py
├── requirements.txt
├── package.json
├── .gitignore
└── README.md
🚀 Installation
Clone Repository
git clone https://github.com/qasimali2512/Insurance-premium-Prediction.git
cd Insurance-premium-Prediction
🐍 Backend Setup

Create a Python virtual environment:

python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn app:app --reload

Backend will run on:

http://127.0.0.1:8000
⚛️ Frontend Setup

Navigate to the frontend directory:

cd insurance-frontend

Install dependencies:

npm install

Start the development server:

npm run dev


🧠 Machine Learning Workflow
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
FastAPI Integration
   ↓
React Frontend
   ↓
Prediction


🔄 Application Workflow
User opens application
        ↓
Enters personal information
        ↓
BMI calculated automatically
        ↓
Clicks "Predict Premium"
        ↓
React sends POST request
        ↓
FastAPI receives request
        ↓
Input validation
        ↓
Feature processing
        ↓
Machine Learning model
        ↓
Prediction generated
        ↓
Confidence calculated
        ↓
Response returned
        ↓
Prediction displayed
