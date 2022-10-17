"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd

#ping http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt
#print(sensor.marin.ntnu.no/logs/Ulstein05_10.txt)c

df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt")

st.bar_chart(df)

st.text("Test")
