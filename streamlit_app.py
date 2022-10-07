"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns


df = pd.read_csv("http://sensor.marin.ntnu.no/logs/Ulstein05_10.txt")

print(df)

