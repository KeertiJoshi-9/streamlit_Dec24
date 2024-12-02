import streamlit as st
import pandas as pd
import datetime
import sklearn
import yfinance as yf

st.title("Stock Price Prediction from yfinance")
c1, c2, c3 = st.columns(3)

with c1:
    stock_name = st.text_input("Input the stock name you want to analyze", "MSFT")

ticker_text = yf.Ticker(stock_name)

with c2:
    startdate = st.date_input("Enter the Start date to display the stock prices:", 
                              datetime.date(2023,12,1))

with c3:
    enddate = st.date_input("Enter the End date to display the stock prices:", 
                              datetime.date(2024,12,1))

ticker_df = ticker_text.history(period='1mo', start=startdate, end=enddate)

st.subheader("Here is the raw day wise stock price.")
st.dataframe(ticker_df)

st.subheader("Here is the line chart for the stock wrt time.")
st.line_chart(ticker_df['Close'])

st.subheader("Here is the volume chart for the stock wrt time.")
st.line_chart(ticker_df['Volume'])