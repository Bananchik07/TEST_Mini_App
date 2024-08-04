import streamlit as st

st.title("ТЕСТ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            <a>
            display: none
            </a>
            """
st.markdown(hide_streamlit_style)
