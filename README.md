# 🧠 Early Chronic Kidney Disease (CKD) Detection System

An end-to-end machine learning-based web application designed to perform **early-stage screening of Chronic Kidney Disease (CKD)** using clinical parameters.

This system leverages multiple machine learning models and an **ensemble approach** to provide reliable and consistent risk predictions.

---

## 📌 Project Overview

Chronic Kidney Disease is a progressive condition that often goes undetected in early stages due to lack of symptoms. This project aims to:

- Identify early CKD risk using patient data
- Provide a fast and accessible screening tool
- Assist in preventive healthcare decisions

The system uses structured clinical inputs and applies machine learning models to predict whether a patient is at risk.

---

## ⚙️ System Workflow
Data Collection → Data Preprocessing → Feature Engineering →
Model Training → Model Evaluation → Ensemble Model → Risk Prediction

---

## 🧪 Machine Learning Approach

Multiple models were trained and evaluated:

- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  

### ✅ Final Model:
**Ensemble Model (Logistic Regression + Random Forest)**

### 🎯 Why Ensemble?
- Improves prediction stability  
- Reduces overfitting  
- Achieves **high recall** (critical in healthcare to avoid missing risk cases)  

---

## 📊 Performance

- Accuracy: ~97%
- High Recall Score (prioritized to detect maximum CKD cases)
- Balanced Precision-Recall tradeoff

---

## 💻 Tech Stack

### 🔹 Backend
- Python
- Flask

### 🔹 Frontend
- HTML
- CSS
- Bootstrap

### 🔹 Machine Learning
- Scikit-learn
- XGBoost
- NumPy
- Pandas
- Joblib (Model Serialization)

---

## 🌐 Features

- User-friendly input form for patient data
- Real-time prediction using trained ML model
- Risk classification (Low / Moderate / High)
- Medical suggestions based on prediction
- Multi-page UI (Home, About, Result)
- Workflow visualization

---

## 📁 Project Structure
ckd_project/ │ ├── app.py ├── ckd_model.pkl ├── features.pkl │ ├── templates/ │   ├── index.html │   ├── result.html │   ├── about.html │ ├── static/ │   ├── images/ │   ├── workflow.png │ └── README.md

sha---

## ⚠️ Disclaimer

This system is intended for **educational and screening purposes only**.  
It does **not replace professional medical diagnosis**.

---

## 👨‍💻 Team Members

- **Shahnawaz Akhtar Fatmee** (Lead Developer)
- **Rameez Rehan**
- **Sadique Ansari**

---

## 🎓 Institution

**Integral University, Lucknow**

---

## 🙏 Acknowledgment

We sincerely express our gratitude to our supervisor:

**Minhajul Afreen Sir**

for his continuous guidance, valuable insights, and support throughout the development of this project.  
His mentorship played a crucial role in shaping both the technical implementation and practical relevance of this system.

---

## ⭐ Future Improvements

- Integration with real hospital datasets
- Deployment on cloud (AWS / Render / Railway)
- Adding more clinical parameters (Creatinine, eGFR)
- Mobile-friendly UI
- AI-based personalized recommendations

---

## 📬 Contact

For queries or collaboration:

📧 Email: shahnawzak@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/shahnawaz-akhtar-388478340  

---

# 🔥 Final Note

This project demonstrates the practical application of machine learning in healthcare screening systems, combining data science with real-world impact.
