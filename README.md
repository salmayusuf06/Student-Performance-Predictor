# 🎓 Student Final Grade Predictor (G3)

A Machine Learning web application built with **Python**, **scikit-learn**, and **Streamlit** to predict a student's final exam grade ($G3$) based on key socio-demographic and academic features.

---

## 📊 Dataset Overview
The model is trained on the Student Performance Dataset. It uses critical academic indicators to forecast outcomes, bypassing non-numeric text variables for optimized Linear Regression training.

### Key Features Used:
* **`G1` & `G2`**: First and second period grades (0–20 scale).
* **`studytime`**: Weekly study time.
* **`failures`**: Number of past class failures.
* **`absences`**: Number of school absences.

---

## 🛠️ Tech Stack
* **Language:** Python
* **ML Library:** scikit-learn (Linear Regression)
* **Web Interface:** Streamlit
* **Deployment Preview:** Localtunnel / Google Colab

---

## 🚀 How to Run Locally

1. **Install dependencies:**
   ```bash
   pip install streamlit scikit-learn pandas joblib
   streamlit run app.py
