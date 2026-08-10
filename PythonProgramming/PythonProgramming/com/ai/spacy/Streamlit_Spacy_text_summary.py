import streamlit as st
import spacy_text_summary as sp_text
default_text ='''Enter your text here.'''
st.title("Spacy Text Summarization")
st.header("Enter your text and generate summary using Spacy.")
user_text = st.text_area("Enter some text here:", key="user_text_area",value=default_text)

if st.button("Generate Summary"):
    current_text = st.session_state.get("user_text_area", "")
    summary = sp_text.generate_user_text_summary(current_text,3)
    # result_summary = " ".join(summary)
    # st.write(result_summary)
    st.text("The summary of your text is:")
    st.write(summary)
else:
    st.write("Button is not clicked.")