import streamlit as st
import pickle
import pandas as pd
import os

# Debugging: List files in directory
st.write("Available files:", os.listdir())

# Load model (check if file exists first)
model_path = "LinearRegressionModel.pkl"
if not os.path.exists(model_path):
    st.error(f"Model file not found: {model_path}")
else:
    model = pickle.load(open(model_path, 'wb'))

    st.title("🚗 Car Price Predictor")
    st.write("Enter the car details to estimate its market value.")

    # Inputs
    name = st.selectbox("Car Name", ["Maruti Swift", "Hyundai i20", "Honda City", "Toyota Innova", "Mahindra XUV", "Tata Nexon", "Kia Seltos", "Ford EcoSport", "Renault Kwid", "Skoda Rapid"])
    company = st.selectbox("Company", ["Maruti", "Hyundai", "Honda", "Toyota", "Mahindra", "Tata", "Kia", "Ford", "Renault", "Skoda"])
    year = st.number_input("Purchase Year", min_value=1990, max_value=2025, step=1, value=2020)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=500, value=10000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

    if st.button("Predict Price"):
        input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Price: ₹ {int(prediction):,}")


