import streamlit as st
import requests

st.set_page_config(page_title="Caprae Lead Qualifier", layout="centered")
st.title("🔍 Caprae AI Lead Qualifier")
st.markdown("Enter a company domain to fetch and score its business lead potential.")

domain = st.text_input("🌐 Company Domain")

if st.button("🎯 Get Lead Insight"):
    if domain:
        with st.spinner("Fetching and scoring lead..."):
            try:
                result = requests.get(f"http://localhost:8000/leadgen?domain={domain}").json()
                st.success("Lead fetched successfully!")
                st.json(result)
            except Exception as e:
                st.error(f"Failed to fetch lead data: {e}")
    else:
        st.warning("Please enter a domain.")