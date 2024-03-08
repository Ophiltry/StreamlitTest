import json
import streamlit as st 
import pandas as pd

with open("test2.json", "r") as f:
    data = json.load(f)

#print(data["name"])

st.write(data["name"])


st.write("blah")



