import streamlit as st
import pickle
import pandas as pd
import os

# Load the cleaned dataset
car = pd.read_csv('Cleaned_Car_data.csv')

# Preprocess name column
car['name'] = car['name'].str.split(' ').str.slice(0, 3).str.join(' ')

# Get unique sorted names
car_names = sorted(car['name'].unique())


# Load model (check if file exists first)
model_path = "LinearRegressionModel.pkl"
if not os.path.exists(model_path):
    st.error(f"Model file not found: {model_path}")
else:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    st.title("🚗 Car Price Predictor")
    st.write("Enter the car details to estimate its market value.")

    # Inputs
    
    # Streamlit dropdown
    selected_name = st.selectbox("Select Car Name", car_names)
    st.write("You selected:", selected_name)
    company = st.selectbox("Company", ["Maruti", "Hyundai", "Honda", "Toyota", "Mahindra", "Tata", "Kia", "Ford", "Renault", "Skoda"])
    year = st.number_input("Purchase Year", min_value=1990, max_value=2025, step=1, value=2020)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=500, value=10000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])

    if st.button("Predict Price"):
        # Apply same 3-word preprocessing to input (in case it's changed manually or reused elsewhere)
        processed_name = ' '.join(selected_name.split(' ')[:3])

        input_df = pd.DataFrame([[processed_name, company, year, kms_driven, fuel_type]],
                        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        try:
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Price: ₹ {int(prediction):,}")
        except ValueError as e:
        st.error(f"⚠️ Error: {str(e)}")




