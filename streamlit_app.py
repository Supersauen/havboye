"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd

headers = []

#ping http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt
#print(sensor.marin.ntnu.no/logs/Ulstein05_10.txt)c

df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt", headers = {'filename', 'power','loc', 'time', 'lat', 'long','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a11','a13'})

st.bar_chart(df)

st.text("Test")
