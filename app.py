import streamlit as st
import joblib
import pandas as pd

# load uploaded model
model = joblib.load("model.pkl")

st.title("Heart Disease Prediction App")

# Create 13 input fields based on the columns of df (excluding the target)
input_data = {}
# Assuming the columns in your training data are in the same order as X_train
feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
for feature in feature_names:
    input_data[feature] = st.number_input(f"Enter value for {feature}")

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

if st.button("Predict"):
    # Make prediction using the loaded model
    pred = model.predict(input_df)

    # Display the prediction
    if pred[0] == 1:
        st.write("Prediction: High probability of Heart Disease")
    else:
        st.write("Prediction: Low probability of Heart Disease")

# You can optionally display Y_test here for comparison or analysis if needed
# st.write("Y_test (for reference):")
# st.write(Y_test)
