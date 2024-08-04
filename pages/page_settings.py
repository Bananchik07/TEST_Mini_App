import streamlit as st

def gif():
    st.image("https://cdn.shopify.com/s/files/1/0344/6469/files/cat-gif-loop-tp.gif?v=1523984593", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# Додавання стилів для зменшення верхнього відступу
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Settings⚙️')

gif()
