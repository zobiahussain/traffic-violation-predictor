import streamlit as st
import lightgbm as lgb
import numpy as np
import pandas as pd

# Load trained model (save it first using joblib)
import joblib
model = joblib.load("model_weather.pkl")

st.title("🚦 Traffic Violation Risk Predictor")

# Input fields
hour = st.slider("Hour of Day", 0, 23, 10)
day = st.slider("Day of Week (0=Mon)", 0, 6, 2)
month = st.slider("Month", 1, 12, 6)
is_weekend = st.selectbox("Is it Weekend?", ["No", "Yes"])
lat = st.number_input("Latitude", value=39.0)
lon = st.number_input("Longitude", value=-77.0)
temp = st.number_input("Temperature (C)", value=20.0)
humidity = st.slider("Humidity", 0.0, 1.0, 0.5)
visibility = st.number_input("Visibility (km)", value=10.0)

# Process inputs
input_data = pd.DataFrame([[
    hour, day, month, 1 if is_weekend == "Yes" else 0,
    lat, lon, temp, humidity, visibility
]], columns=[
    'hour', 'day_of_week', 'month', 'is_weekend',
    'Latitude', 'Longitude', 'Temperature (C)', 'Humidity', 'Visibility (km)'
])

# Predict
prediction = model.predict(input_data)[0]
label = "⚠️ High Risk (Serious Violation Likely)" if prediction == 1 else "✅ Low Risk"

# Show result
st.subheader("Prediction:")
st.success(label)
