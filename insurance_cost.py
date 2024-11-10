import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Insurance Premium Cost Prediction")
insurance_df = pd.read_csv("./Insurance_data.csv")
st.dataframe(insurance_df.head())

st.header("Please fill in your details")

with open('insurance_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('insurance_model.pkl', 'rb') as rf_model_file:
    best_rf_model = pickle.load(rf_model_file)

# Age input
age = st.slider("How old are you?", 18, 66, step=1)

# Columns for Height, Weight, and Number of Major Surgeries
col1, col2, col3 = st.columns(3)
with col1:
    height = st.number_input("Height (cm):", min_value=140, max_value=190, step=1)
with col2:
    weight = st.number_input("Weight (kg):", min_value=50, max_value=135, step=1)
with col3:
    num_surgeries = st.selectbox("Number of Major Surgeries:", options=[0, 1, 2, 3])

# BMI calculation (Height in cm, Weight in kg)
bmi = weight / ((height / 100) ** 2)
st.markdown(f"**Your calculated BMI is:** {bmi:.1f}")

# Binary inputs using checkboxes for Yes/No questions
diabetes = 1 if st.checkbox("Do you have Diabetes?") else 0
bp_problems = 1 if st.checkbox("Do you have Blood Pressure Problems?") else 0
transplants = 1 if st.checkbox("Have you had any Transplants?") else 0
chronic_diseases = 1 if st.checkbox("Do you have any Chronic Diseases?") else 0
allergies = 1 if st.checkbox("Do you have Known Allergies?") else 0
cancer_history = 1 if st.checkbox("Is there a History of Cancer in your Family?") else 0


def model_pred(Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies,
               HistoryOfCancerInFamily, NumberOfMajorSurgeries, BMI):
    # Ensure the order of features matches the trained model's input
    input_features = pd.DataFrame([[Age, Height, Weight, BMI, Diabetes, BloodPressureProblems, AnyTransplants, 
                                    AnyChronicDiseases, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries]], 
                        columns=['Age', 'Height', 'Weight', 'BMI', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants', 
                                 'AnyChronicDiseases', 'KnownAllergies', 'HistoryOfCancerInFamily', 'NumberOfMajorSurgeries'])

    # Columns that need to be scaled
    numerical_cols = ['Age', 'Height', 'Weight', 'BMI']
    input_features_scaled = input_features.copy()
    input_features_scaled[numerical_cols] = scaler.transform(input_features[numerical_cols])

    # Make prediction using the pre-trained model
    return best_rf_model.predict(input_features_scaled)

if st.button('Predict the Premium Price'):
    # Call model prediction with BMI calculated from Height and Weight
    Premium_Price = model_pred(age, diabetes, bp_problems, transplants, chronic_diseases, height, weight, allergies,
                               cancer_history, num_surgeries, bmi)
    st.text(f'The premium price is {(Premium_Price[0]):.2f}')
