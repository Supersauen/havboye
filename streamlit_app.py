"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd



df = pd.read_txt("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt")

print(df)

