import streamlit as st


# 1. Define the function that adds the tab to your list
def show_demo_tab(tab_titles):
    tab_titles.append("Demo Tab")


# 2. Initialize the state tracker
if "tab_is_visible" not in st.session_state:
    st.session_state.tab_is_visible = False

# Base tabs that are always there
tab_titles = ["Home", "Settings"]

# 3. Use the button to toggle the session state variable
if st.button("Show / Hide Tab"):
    st.session_state.tab_is_visible = not st.session_state.tab_is_visible

# 4. Trigger your function if the state is True
if st.session_state.tab_is_visible:
    show_demo_tab(tab_titles)

# 5. Render the tabs safely
tabs = st.tabs(tab_titles)

with tabs:
    st.write("Main content")
with tabs:
    st.write("Settings content")

# Only fill the demo tab if it exists in the list
if st.session_state.tab_is_visible:
    with tabs:
        st.write("Welcome to the Demo Tab!")
