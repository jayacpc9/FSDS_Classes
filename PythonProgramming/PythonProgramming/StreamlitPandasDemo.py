import streamlit as st
import pandas as pd
import numpy as np
import toml

# 1. Paste your exact TOML configuration inside a multi-line Python string
toml_config_data = """
[theme]
base="light"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
primaryColor="#FF4B4B"
"""

# 2. Parse the string data into a standard Python dictionary
# config_dict = toml.loads(toml_config_data)
#
# st.set_option("theme.primaryColor", config_dict["theme"]["primaryColor"])
# st.set_option("theme.backgroundColor", config_dict["theme"]["backgroundColor"])

tab_titles = ["Cats", "Dogs", "Owls"]
tab_urls = ["https://static.streamlit.io/examples/cat.jpg", "https://static.streamlit.io/examples/dog.jpg",
            "https://static.streamlit.io/examples/owl.jpg"]
tab_content_captions = ["A cute cat", "A good dog", "A beautiful Owl"]
tab_subheader_title = ["This is Cats Tab", "This is Dogs Tab", "This is Owls Tab"]


def show_demo_tab():
    # add a tab in the main page.
    all_tabs = st.tabs(tab_titles)
    for index, tab in enumerate(all_tabs):
        with tab:
            st.subheader("sub header : "+tab_subheader_title[index])
            st.write("# "+tab_subheader_title[index])
            st.image(tab_urls[index], caption=tab_content_captions[index])
    # End of Tab


def show_demo_tab_in_sidebar():
    # add a tab in the sidebar.
    tab1, tab2, tab3 = st.sidebar.tabs(["Cats", "Dogs", "Owls"])
    with tab1:
        st.subheader("# This is Cats Tab")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=300, caption="A cute dog")
    with tab2:
        st.subheader("# This is Dogs Tab")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=300, caption="A cute dog")
    with tab3:
        st.subheader("# This is Owls Tab")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=300, caption="A cute dog")
    # End of Tab

logo_icon = "https://www.streamlit.io/images/brand/streamlit-mark-color.svg"
logo_full = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg"
st.logo(logo_full, link="https://streamlit.io", icon_image=logo_icon, size="large")

st.title("Streamlit Pandas Demo")
st.write("""This is a sample app to demo pandas and numpy""")

st.title("ST Title Demo")

st.sidebar.title("📊 Analytics Dashboard")
st.sidebar.subheader("Streamlit sidebar subheader")

st.sidebar.write("Enter your name")
user_name = st.sidebar.text_input("Enter your age", "Jaya")

st.sidebar.header("Select a Number")
slider = st.sidebar.slider("Picka a number ", min_value=0, max_value=100, value=25)

show_demo_tab_in_sidebar()

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
    st.write(data)  # Show the same data as previous table

if st.button("Say Hello"):
    st.write(f"""Hello ! {user_name}""")
else:
    st.write("""Click the button to say Hello!""")

if st.button("Show Tab"):
    show_demo_tab()


