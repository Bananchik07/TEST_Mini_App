import streamlit as st

# CSS для прозорого фону та контуру кнопок
custom_css = """
    <style>
    .stButton > button {
        background-color: transparent;
        border: 2px solid transparent;
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: rgba(0, 0, 0, 0.1);
        border: 2px solid #000000;
    }
    .stButton > button:active {
    color: white;
    background-color: grey;
    }
    </style>
"""

# Додавання стилів
st.markdown(custom_css, unsafe_allow_html=True)

st.sidebar.title("Main menu")
st.sidebar.button("Account♿", type="primary")
st.sidebar.button("My courses📝", type="primary")
st.sidebar.button("Find course🔍", type="primary")
st.sidebar.button("Settings⚙️", type="primary")



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
