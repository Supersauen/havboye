"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np



df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt")

print(df)

