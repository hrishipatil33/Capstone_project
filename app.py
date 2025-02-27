import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the saved model
model = joblib.load('best_car_price_model.pkl')

# Function to make predictions
def predict_price(year, km_driven, fuel, seller_type, transmission, owner):
    data = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner]
    })
    
    prediction = model.predict(data)
    return prediction[0]

# Streamlit web app layout
st.title('Car Price Prediction App')
st.write("Predict the selling price of a used car based on its characteristics")

# User input fields
year = st.number_input('Year of Manufacture', min_value=1990, max_value=2024, value=2015)
km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=1000000, value=50000)
fuel = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])

# Predict button
if st.button('Predict Price'):
    result = predict_price(year, km_driven, fuel, seller_type, transmission, owner)
    st.success(f"The predicted selling price of the car is: ₹ {np.round(result, 2)}")
