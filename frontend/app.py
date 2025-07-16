import streamlit as st
import requests

st.title("Iris Flower Classifier")

sepal_length = st.number_input("Sepal Length", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width", 0.0, 10.0, 0.2)

if st.button("Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    response = requests.post(
        "http://backend:5000/predict",
        json={"feature_array": features}
    )
    if response.status_code == 200:
        pred = response.json()["prediction"][0]
        st.success(f"Predicted class: **{pred}**")
    else:
        st.error("Prediction failed.")