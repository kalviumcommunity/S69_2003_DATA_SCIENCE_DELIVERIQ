import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model

model = pickle.load(
    open("../models/delivery_time_model.pkl", "rb")
)

# App title

st.title("🚚 DeliverIQ")

st.subheader("Food Delivery Time Prediction System")

st.write(
    """
    This machine learning application predicts
    estimated food delivery time based on
    delivery conditions.
    """
)

# User Inputs

delivery_person_age = st.number_input(
    "Delivery Person Age",
    min_value=18,
    max_value=60,
    value=25
)

delivery_person_ratings = st.number_input(
    "Delivery Person Ratings",
    min_value=1.0,
    max_value=5.0,
    value=4.5
)

distance = st.number_input(
    "Distance",
    min_value=0.0,
    value=5.0
)

# Vehicle Type

vehicle_type = st.selectbox(
    "Type of Vehicle",
    ["motorcycle", "scooter"]
)

# Order Type

order_type = st.selectbox(
    "Type of Order",
    ["Snack", "Drinks", "Buffet", "Meal"]
)

# Prediction Button

if st.button("Predict Delivery Time"):

    # Create input dataframe

    input_data = pd.DataFrame({
        "Delivery_person_Age": [delivery_person_age],
        "Delivery_person_Ratings": [delivery_person_ratings],
        "Restaurant_latitude": [0],
        "Restaurant_longitude": [0],
        "Delivery_location_latitude": [0],
        "Delivery_location_longitude": [0],
        "distance": [distance],
        "Type_of_order_Drinks": [1 if order_type == "Drinks" else 0],
        "Type_of_order_Meal": [1 if order_type == "Meal" else 0],
        "Type_of_order_Snack": [1 if order_type == "Snack" else 0],
        "Type_of_vehicle_scooter": [1 if vehicle_type == "scooter" else 0]
    })

    # Make prediction

    prediction = model.predict(input_data)

    # Display result

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )

    