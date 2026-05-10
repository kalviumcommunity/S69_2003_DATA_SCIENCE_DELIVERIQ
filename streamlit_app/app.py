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

    # Load training columns

    model_columns = pickle.load(
        open("../models/model_columns.pkl", "rb")
    )

    # Create empty dataframe with training columns

    input_data = pd.DataFrame(
        columns=model_columns
    )

    # Add one empty row

    input_data.loc[0] = 0

    # Fill numeric values

    input_data["Delivery_person_Age"] = delivery_person_age

    input_data["Delivery_person_Ratings"] = delivery_person_ratings

    input_data["distance"] = distance

    # Encode vehicle type

    vehicle_column = f"Type_of_vehicle_{vehicle_type}"

    if vehicle_column in input_data.columns:
        input_data[vehicle_column] = 1

    # Encode order type

    order_column = f"Type_of_order_{order_type}"

    if order_column in input_data.columns:
        input_data[order_column] = 1

    # Make prediction

    prediction = model.predict(input_data)

    # Display result

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )