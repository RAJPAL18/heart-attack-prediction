import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("❤️ Heart Attack Prediction App")

st.write("Enter patient details to check the risk of heart attack.")

# Input fields with full names and integer values
age = st.number_input("Age (years)", min_value=1, max_value=120, step=1)

sex = st.radio("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

cp = st.number_input("Chest Pain Type (0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic)", 
                     min_value=0, max_value=3, step=1)

trestbps = st.number_input("Resting Blood Pressure (in mm Hg)", min_value=80, max_value=200, step=1)

chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)

fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

restecg = st.number_input("Resting Electrocardiographic Results (0: Normal, 1: ST-T abnormality, 2: Left ventricular hypertrophy)", 
                          min_value=0, max_value=2, step=1)

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, step=1)

exang = st.radio("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest (oldpeak)", 
                          min_value=0, max_value=6, step=1)

slope = st.number_input("Slope of the Peak Exercise ST Segment (0: Upsloping, 1: Flat, 2: Downsloping)", 
                        min_value=0, max_value=2, step=1)

ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0–4)", min_value=0, max_value=4, step=1)

thal = st.number_input("Thalassemia (1: Normal, 2: Fixed Defect, 3: Reversible Defect)", 
                       min_value=0, max_value=3, step=1)

# Collect input
input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                          columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of Heart Attack")
    else:
        st.success("✅ Low risk of Heart Attack")
