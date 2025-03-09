import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("📊 Student Score Prediction")
st.write("Enter values to predict the total score.")

# Ensure 14 input fields match the model
P1 = st.number_input("P1", value=50)
C1 = st.number_input("C1", value=25.0)
P2 = st.number_input("P2", value=50)
C2 = st.number_input("C2", value=25.0)
P3 = st.number_input("P3", value=50)
C3 = st.number_input("C3", value=25.0)
R1 = st.number_input("R1", value=10.0)
T1 = st.number_input("T1", value=5.0)
P3T = st.number_input("P3T", value=25.0)
Extra1 = st.number_input("Extra1", value=0.0)  # Add missing features
Extra2 = st.number_input("Extra2", value=0.0)
Extra3 = st.number_input("Extra3", value=0.0)
Extra4 = st.number_input("Extra4", value=0.0)
Extra5 = st.number_input("Extra5", value=0.0)

# Predict button
if st.button("Predict Total Score"):
    input_data = np.array([[P1, C1, P2, C2, P3, C3, R1, T1, P3T, Extra1, Extra2, Extra3, Extra4, Extra5]])
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Total Score: {prediction:.2f}")

