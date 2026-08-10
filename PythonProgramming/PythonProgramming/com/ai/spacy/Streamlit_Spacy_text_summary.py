import streamlit as st
import spacy_text_summary as sp_text
default_text =''' There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.'''
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