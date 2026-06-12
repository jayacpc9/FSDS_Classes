import streamlit as st
from ollama import Client
MY_HOST ="http://localhost:11434"
MODEL ="deepseek-r1:1.5b"
# MODEL ="kimi-k2.5:cloud"
client = Client(host = MY_HOST)

st.set_page_config(
    page_title = "Custom LLM model -Ollama",
    layout = "centered"
)

st.title("My Text - Ollama App")
prompt = st.text_are("Enter you prompt : ", height = 200)
if st.button("Generate Response"):
    if prompt.strip() ==MODEL:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model = MODEL,
                message=[
                   {"role": "user", "content": prompt}
                ]
            )

            st.success("response connected!")
