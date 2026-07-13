import streamlit as st
import pandas as pd
import joblib
model = joblib.load("../delay_model.pkl")
st.title("Airline Delay Prediction System")
airline=st.selectbox("Airline",["Air India","IndiGo","SpiceJet","Vistara"])
distance=st.number_input("Distance")
hour=st.number_input("Departure Hour")
weather=st.selectbox("Weather",["Sunny","Cloudy","Rain","Fog"])

if st.button("Predict"):
    result=model.predict([[1,1,1,hour,distance,1]])
    if result[0]==1:
        st.error("Flight Delayed")
    else:
        st.success("Flight On Time")