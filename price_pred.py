import streamlit as st
import pandas as pd
import sklearn
import pickle

st.title("Price Prediction of cars")

cars_df = pd.read_csv("C:/Users/Keerti Joshi/Documents/GitHub/streamlit_Dec24/cars24-car-price-cleaned.csv")

st.dataframe(cars_df.head())

with open('C:/Users/Keerti Joshi/Documents/GitHub/streamlit_Dec24/model.pkl', 'rb') as f:
    model = pickle.load(f)