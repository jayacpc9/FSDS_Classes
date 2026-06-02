import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Pandas Demo")
st.write("""This is a sample app to demo pandas and numpy""")

st.sidebar.subheader("Streamlit sidebar")
st.sidebar.write("Enter your name")
user_name = st.sidebar.text_input("Enter your age", "Jaya")

st.sidebar.header("Select a Number")
slider = st.sidebar.slider("Picka a number ", min_value=0, max_value=100, value=25)

favorite_color = st.sidebar.selectbox("What is your favorite color?", ["Blue", "Red", "Green", "Yellow"])
print("favorite_color+"".lower() == ", favorite_color.lower())
st.sidebar.write(f"### Your favorite :red[color] is: :{favorite_color.lower()}[**{favorite_color}**]")
# st.write(f"### :{favorite_color.lower()}[**{favorite_color}**]")

st.header(f"Welcome, {user_name}!")
st.write(f"### Your favorite color is :{favorite_color.lower()}[**{favorite_color}**]")
st.write(f"### Your Picked number : **{slider}**")

st.subheader("Here's some random data:")

# Create a sample DataFrame
data = pd.DataFrame(slider * np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
st.dataframe(data)

if st.checkbox("Show more random data"):
    st.subheader("Raw Data")
    st.write(data)#Show the same data as previous table


if st.button("Say Hello"):
    st.write(f"""Hello ! {user_name}""")
else:
    st.write("""Click the button to say Hello!""")