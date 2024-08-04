import streamlit as st

st.title("ТЕСТ")

VIDEO_URL = "https://vss6.coursehunter.net/s/c7119c234f428763529be8af167d21ad/udemy-megapython/lesson1.mp4"
st.video(VIDEO_URL)

st.sidebar.title("Бічна панель")
st.sidebar.selectbox("Виберіть опцію", ["Опція 1", "Опція 2"])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


