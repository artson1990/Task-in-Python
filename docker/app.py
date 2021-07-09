import streamlit as st
from datetime import date

import yfinance as yf

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction APP")

stocks = ("AAPL", "GOOG", "MSFT", "AMZN", "TSLA", "BAC", "BMW.TI" "XELA", "NEGG", "DARE")
selected_stock = st.selectbox("Select dateset for perdiction", stocks)

n_years = st.slider("Years of perdiction:", 1 , 4)
period = n_years * 365

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data..")
data = load_data(selected_stock)
data_load_state.text("Loading date...Done!")

st.subheader('Raw data')
st.write(data.tail())
    

