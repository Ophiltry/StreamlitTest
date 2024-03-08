import json
import streamlit as st 
import pandas as pd

with open("test2.json", "r") as f:
    data = json.load(f)

#print(data["name"])

#st.write(data["name"])


#st.write("blah")

st.balloons()



col1, col2, col3 = st.columns([3,3,3], gap="large")

with col1:
   st.header("Name" , divider="red")
   st.write(data["name"])

with col2:
   st.header("Age")
   st.write(data["age"])

with col3:
   st.header("Language")
   st.write(data["languages"])

