import streamlit as st

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

def gif():
    for _ in range(6):
        st.image(
            "https://cdn.shopify.com/s/files/1/0344/6469/files/cat-gif-loop-wheel_grande.gif?v=1523982721", 
            caption=None, 
            width=None, 
            use_column_width=None, 
            clamp=False, 
            channels="RGB", 
            output_format="auto"
        )

st.title('Find course🔍')

# Додаємо два випадаючих списки в один рядок
col1, col2 = st.columns(2)

with col1:
    option1 = st.selectbox('Виберіть опцію 1:', ['Опція 1', 'Опція 2', 'Опція 3'])

with col2:
    option2 = st.selectbox('Виберіть опцію 2:', ['Опція A', 'Опція B', 'Опція C'])

gif()
