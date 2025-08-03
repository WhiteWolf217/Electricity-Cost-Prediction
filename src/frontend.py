import streamlit as st
import requests

st.title("Electricity Cost Prediction")

site_area = st.number_input("Site Area (sq meters)")
water_consumption = st.number_input("Water Consumption (liters/day)")
recycling_rate = st.number_input("Recycling Rate (%)")
utilisation_rate = st.number_input("Utilisation Rate (%)")
air_qality_index = st.number_input("Air Quality Index (AQI)")
issue_reolution_time = st.number_input("Issue Resolution Time (hours)")
resident_count = st.number_input("Resident Count (number of people)")

st.markdown("### Structure Type (One-hot encoded)")
structure_type_Commercial = st.number_input("Commercial (0 or 1)")
structure_type_Industrial = st.number_input("Industrial (0 or 1)")
structure_type_Mixed_use = st.number_input("Mixed-use (0 or 1)")
structure_type_Residential = st.number_input("Residential (0 or 1)")

if st.button("Predict"):
    payload = {
        "site_area": site_area,
        "water_consumption": water_consumption,
        "recycling_rate": recycling_rate,
        "utilisation_rate": utilisation_rate,
        "air_qality_index": air_qality_index,
        "issue_reolution_time": issue_reolution_time,
        "resident_count": resident_count,
        "structure_type_Commercial": structure_type_Commercial,
        "structure_type_Industrial": structure_type_Industrial,
        "structure_type_Mixed_use": structure_type_Mixed_use,
        "structure_type_Residential": structure_type_Residential
    }

    # response = requests.post("http://127.0.0.1:8000/predict", json=payload)  # Local testing
    response = requests.post("https://electricity-cost-prediction-luz2.onrender.com/predict", json=payload)

    st.write("💡 **Predicted Electricity Cost (USD/month):**", response.json()["predicted_electricity_cost"])
