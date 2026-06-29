import streamlit as st
import pandas as pd
import joblib
import os

st.title("🎓 Student Final Grade Predictor (G3)")
st.write("This application predicts a student's final exam score based on academic indicators[cite: 15, 21].")

if not os.path.exists("models/student_model.pkl"):
    st.error("⚠️ Model file not found! Please run the training cells above first.")
else:
    model = joblib.load("models/student_model.pkl")
    features = joblib.load("models/features.pkl")

    st.header("📊 Input Student Parameters")
    
    # User-friendly inputs for the most important grade factors
    studytime = st.slider("Weekly Study Time (1 = <2 hours, 2 = 2-5 hours, 3 = 5-10 hours, 4 = >10 hours)", 1, 4, 2)
    failures = st.slider("Number of Past Class Failures", 0, 4, 0)
    absences = st.slider("Number of School Absences", 0, 93, 4)
    g1 = st.slider("First Period Grade (G1 Score: 0 - 20)", 0, 20, 10)
    g2 = st.slider("Second Period Grade (G2 Score: 0 - 20)", 0, 20, 10)

    # Automatically fill any remaining default numeric features with their median/average values
    input_dict = {col: 3 for col in features}  # default neutral value
    input_dict.update({
        'studytime': studytime,
        'failures': failures,
        'absences': absences,
        'G1': g1,
        'G2': g2,
        'age': 16,
        'Medu': 2,
        'Fedu': 2,
        'traveltime': 1,
        'famrel': 4,
        'freetime': 3,
        'goout': 3,
        'Dalc': 1,
        'Walc': 1,
        'health': 3
    })

    # Convert to DataFrame matching the exact training columns order
    input_data = pd.DataFrame([input_dict])[features]

    if st.button("🔮 Predict Final Grade (G3)"):
        prediction = model.predict(input_data)[0]
        final_score = max(0, min(20, prediction)) # Bounded between 0 and 20 based on dataset rules
        st.success(f"### Predicted Final Grade: **{final_score:.2f} / 20**")
