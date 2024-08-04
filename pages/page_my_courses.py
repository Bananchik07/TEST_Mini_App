import streamlit as st

def gif():
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHMyYWxrdnMybnZzaWpxYWRtaTIwazJ2eWhhcTljbzZwc2I3cGM2byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gKfNj8cYeGN63bLRkF/giphy.webp", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

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

st.title('My courses📝')

gif()
