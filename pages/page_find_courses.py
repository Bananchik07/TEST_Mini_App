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
        # HTML та CSS для стилізації кнопки
        button_html_with_image_responsive = """
        <style>
            .button-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
                margin-top: 20px;
            }
            .course-button {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                border: 2px solid #262730;
                border-radius: 8px;
                width: 100%;
                max-width: 800px;
                height: 150px;
                padding: 10px;
                background-color: #10131A;
                text-align: left;
                cursor: pointer;
                box-sizing: border-box;
            }
            .course-button:hover {
                background-color: #141921;
            }
            .course-image {
                width: 80px;
                height: 80px;
                margin-right: 10px;
            }
            .course-content {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                width: calc(100% - 90px);  /* Adjusted to fit the image width and margin */
            }
            .course-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .course-description {
                flex-grow: 1;
                font-size: 16px;
                margin-bottom: 10px;
            }
            .course-price {
                text-align: right;
                font-size: 20px;
                font-weight: bold;
                color: #2A8018;
            }
        </style>
        
        <div class="button-container">
            <div class="course-button" onclick="window.location.href='#'">
                <img src="https://via.placeholder.com/120" class="course-image" alt="Course Image">
                <div class="course-content">
                    <div class="course-title">Course name</div>
                    <div class="course-description">description</div>
                    <div class="course-price">$$$</div>
                </div>
            </div>
        </div>
        """

        # Відображення кнопки у Streamlit
        st.markdown(button_html_with_image_responsive, unsafe_allow_html=True)

st.title('Find course🔍')

# Додаємо два випадаючих списки в один рядок
col1, col2 = st.columns(2)

with col1:
    option1 = st.selectbox('Choose category:', ['XXX', 'Anal', 'Gay'])

with col2:
    option2 = st.selectbox('Choose lang🌎:', ['Eng', 'Rus'])

gif()
