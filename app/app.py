import streamlit as st
from app_pages import Home, Predict, Performance

st.set_page_config(page_title="Fruitifier", layout="wide")

page = st.sidebar.selectbox("Navigation", ["Home", "Predict", "Model Performance"])

if page == "Home":
    Home.show()
elif page == "Predict":
    Predict.show()
elif page == "Model Performance":
    Performance.show()