import streamlit as st
import base64

def set_background():
    with open("background.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image:
        linear-gradient(rgba(5,8,22,.75), rgba(5,8,22,.80)),
        url("data:image/png;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)