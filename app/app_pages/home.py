import streamlit as st

def show():
    st.title("🍎 Welcome to Fruitifier")
    st.write("""
        **Fruitifier** is a deep learning-powered tool that can recognize fruits from uploaded photos.

        Upload an image of a fruit and let the AI tell you what it is!
        
        🔍 Built using TensorFlow, Streamlit, and a Convolutional Neural Network (CNN).
    """)
    st.image("", use_column_width=True)