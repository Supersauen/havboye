"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd

headers = []


df4 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
df2 = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein17_10.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])


st.header("Bøye nr 2 test")
#st.bar_chart(df2[['lat','lon']])
st.dataframe(df2)
st.map(df2)

st.header("Bøye nr 4 test")
#st.bar_chart(df[['lat','lon']])
st.dataframe(df4)
st.map(df4)






#st.text("Test")
