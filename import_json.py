import json
import streamlit as st 
import pandas as pd

with open("test2.json", "r") as f:
    data = json.load(f)

#print(data["name"])

#st.write(data["name"])


#st.write("blah")
st.set_page_config(
    page_title="Test Website",
    layout="wide"
)
st.balloons()
st.header("JSON test")


col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1], gap="large")

with col1:
   st.header("Name" , divider="red")
   st.write(data["name"])
   st.write(data["name"])
   st.write(data["name"])

with col2:
   st.header("Age" , divider="orange")
   st.write(data["age"])

with col3:
   st.header("Language" , divider="orange")
   st.write(data["languages"])

with col4:
   st.header("Fun header" , divider="green")
   st.write("fun")

with col5:
   st.header("Fun header" , divider="blue")
   st.write("mo fun")

st.header("JSON test bottom header", divider="blue")
