import os
import pickle
import pandas as pd
import streamlit as st



# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="DeliverIQ",
    page_icon="🚚",
    layout="centered"
)

# ---------------------------------------------------
# Load Model & Training Columns
# ---------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

model_path = os.path.join(
    BASE_DIR,
    "models",
    "delivery_time_model.pkl"
)

columns_path = os.path.join(
    BASE_DIR,
    "models",
    "model_columns.pkl"
)

model = pickle.load(open(model_path, "rb"))

model_columns = pickle.load(open(columns_path, "rb"))

# ---------------------------------------------------
# App Title
# ---------------------------------------------------

st.title("🚚 DeliverIQ")

st.subheader("Food Delivery Time Prediction System")

st.write(
    """
    Predict estimated food delivery time using
    machine learning based on delivery conditions.
    """
)

st.markdown("---")

# ---------------------------------------------------
# User Inputs
# ---------------------------------------------------

delivery_person_age = st.number_input(
    "Delivery Person Age",
    min_value=18,
    max_value=60,
    value=25
)

delivery_person_ratings = st.slider(
    "Delivery Person Ratings",
    min_value=1.0,
    max_value=5.0,
    value=4.5,
    step=0.1
)

distance = st.number_input(
    "Distance (in km)",
    min_value=0.0,
    value=5.0
)

# ---------------------------------------------------
# Vehicle Type
# ---------------------------------------------------

vehicle_type = st.selectbox(
    "Type of Vehicle",
    [
        "motorcycle",
        "scooter",
        "electric_scooter"
    ]
)

# ---------------------------------------------------
# Order Type
# ---------------------------------------------------

order_type = st.selectbox(
    "Type of Order",
    [
        "Snack",
        "Drinks",
        "Buffet",
        "Meal"
    ]
)

st.markdown("---")

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("Predict Delivery Time"):

    # Create empty dataframe with all training columns

    input_data = pd.DataFrame(
        columns=model_columns
    )

    # Add single empty row

    input_data.loc[0] = 0

    # Fill numerical columns

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
        f"🚀 Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )

    # Additional insights

    if prediction[0] <= 20:
        st.info("⚡ Fast delivery expected")

    elif prediction[0] <= 40:
        st.info("🛵 Moderate delivery time expected")

    else:
        st.warning("⏳ Possible delivery delay expected")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "Built using Streamlit & Machine Learning | DeliverIQ"
)