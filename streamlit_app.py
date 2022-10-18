"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd

headers = []


df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
st.header("Bar_chart_test")
st.bar_chart(df[['lat','lon']])
st.dataframe(df)

st.map(df)

st.text("Test")
