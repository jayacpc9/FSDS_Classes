import math

import streamlit as st
st.title("Streamlit Demo app")
st.write("""Welcome! This app calculates the square of a number and square root also""")

st.header("Select a Number")
number =st.slider("Select a Number",0,50,5)

st.subheader("Result")
squared_number = number*number
st.write(f"The square of **{number}** is **{squared_number}**")
st.write(f"The square root of {number} is : {math.sqrt(number)}")
