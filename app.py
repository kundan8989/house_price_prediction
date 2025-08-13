import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load("house_price_prediction.pkl")  # Change filename if needed


st.title("🏠 House Price Prediction")

st.write("Enter the details of the house below:")

# Input fields
area = st.number_input("Area (in sq ft)", min_value=100, max_value=10000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, step=1)
floors = st.number_input("Number of Floors", min_value=1, max_value=5, step=1)
year_built = st.number_input("Year Built", min_value=1800, max_value=2025, step=1)
location = st.selectbox("Location", ["Downtown", "Suburbs",'Urban', "Rural"])  
condition = st.selectbox("Condition", [ "Excellent", "Good",'Fair','Poor'])
garage = st.selectbox("Garage", ["No", "Yes"])

# Encode categorical values if your model needs it
location_map = {"Downtown": 1, "Suburbs": 2,'Urban':3, "Rural": 4}
condition_map = {"Excellent": 1,"Good": 2,"Fair": 3, "Poor": 4}
garage_map = {"No": 0, "Yes": 1}

# Prepare input for prediction
input_data = np.array([[
    area,
    bedrooms,
    bathrooms,
    floors,
    year_built,
    location_map[location],
    condition_map[condition],
    garage_map[garage]
]])

if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ₹{price:,.2f}")
