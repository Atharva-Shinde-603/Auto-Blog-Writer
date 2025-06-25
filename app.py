import streamlit as st
import requests

st.title("Your AI Powered Blog Writer Assistant")
topic=st.text_input("Please Enter Blog Topic: ")

if st.button("Generate Blog"):
    with st.spinner("Generating Your Blog..."):
        response = requests.post("http://127.0.0.1:5000/generate_blog", json={"topic":topic})

        if response.status_code==200:
            result=response.json()
            st.subheader("Generated Your Blog: ")
            st.markdown(result["blog"])
        else:
            st.error("Error Generating Blog! ")
