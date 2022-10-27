import streamlit as st
import numpy as np
import pandas as pd

headers = []

df1 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB1.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
#df2 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB2.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
df3 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB3.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
#df4 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB4.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])
df5 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB5.txt", names = ['filename', 'power','loc', 'time', 'lat', 'lon','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13'])

st.header("Bøye nr 1")
st.dataframe(df1)
st.map(df1)

'''
st.header("Bøye nr 2")
st.dataframe(df2)
st.map(df2)

'''
st.header("Bøye nr 3")
st.dataframe(df3)
st.map(df3)
'''

st.header("Bøye nr 4")
st.dataframe(df4)
st.map(df4)
'''

st.header("Bøye nr 5")
st.dataframe(df5)
st.map(df5)

