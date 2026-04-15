# 🛡️ ReturnShield AI

AI-powered system to detect fraudulent e-commerce return behavior using machine learning and behavioral analysis.

---

## 🚀 Overview

ReturnShield AI analyzes customer return patterns and transaction behavior to identify potentially fraudulent return activities in e-commerce platforms.

This project simulates a real-world fraud detection system with a production-ready architecture including:

* Machine Learning model
* FastAPI backend (deployed)
* Streamlit frontend
* Real-time API integration

---

## 🧠 Key Features

* 🔍 Fraud probability prediction
* ⚠️ Risk classification (Low / Medium / High)
* 🌐 Live deployed backend (Render)
* 🎨 Interactive frontend (Streamlit)
* 📊 Synthetic but realistic dataset
* ⚡ Fast API-based predictions

---

## 🏗️ System Architecture

User → Streamlit UI → FastAPI Backend → ML Model → Prediction

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Features:

  * Return ratio
  * Account age
  * Order value
  * Return frequency
  * Product category
  * Return reason

---

## 📈 Performance

* Accuracy: ~82%
* Recall (Fraud Detection): ~86%
* Optimized for catching fraudulent behavior

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* FastAPI
* Streamlit
* Pandas / NumPy
* Joblib

---

## ▶️ Run Locally

### 1. Clone repo

git clone https://github.com/biman2006/ReturnShield_AI.git

cd ReturnShield_AI

---

### 2. Create virtual environment

python -m venv venv

venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Run backend

uvicorn app.main:app --reload

---

### 5. Run frontend

streamlit run frontend/app.py

---

## 🌐 Live Demo

Backend API (Render):
https://returnshield-ai.onrender.com/predict

Frontend (Streamlit):
https://returnshieldai-appnz55zea6mjvzdqcplwga.streamlit.app/

---

## 📁 Project Structure

ReturnShield AI/
│
├── app/                # FastAPI backend
├── frontend/           # Streamlit UI
├── model/              # Trained model
├── data/               # Dataset
├── requirements.txt
├── Procfile
└── README.md

---

## 🔒 Real-World Considerations

* Backend-controlled feature generation (prevents fake input)
* Behavioral pattern analysis instead of static checks
* Scalable API-based architecture
* Ready for database integration

---

## 🚀 Future Improvements

* Database integration (PostgreSQL)
* User authentication system
* Real-time monitoring dashboard
* Explainable AI (SHAP)
* Payment fraud integration

---

## 💡 Use Cases

* E-commerce platforms (Flipkart, Myntra, Shopify stores)
* Fraud prevention systems
* Return abuse detection
* Risk scoring engines

---

## 👨‍💻 Author

Biman Adhikary

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it 🚀
