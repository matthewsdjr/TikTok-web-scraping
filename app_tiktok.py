import streamlit as st 
import pandas as pd 
from tiktok_2 import get_data
from subprocess import call
from tikapi import TikAPI, ValidationException, ResponseException
import sys
import os

# Input
hashtag = st.text_input('Search for a hashtag here:', value="")

# Button
if st.button('Get Data'):
    # Run get data function here
    st.write(hashtag)
    call(['python', 'tiktok_2.py', hashtag])

# Load in existing data to test it out
df = pd.read_csv('data_final.csv')
# Show tabular dataframe in streamlit
df