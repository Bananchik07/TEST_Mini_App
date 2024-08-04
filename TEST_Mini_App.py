import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#st.set_page_config(page_title='Green Coffee in the USA', page_icon='☕️', layout='wide', initial_sidebar_state='expanded')

pages = [st.Page('pages/page_account.py',title='Account♿', default=True), 
         st.Page('pages/page_my_courses.py',title='My courses📝'), 
         st.Page('pages/page_find_courses.py',title='Find course🔍'), 
         st.Page('pages/page_settings.py',title='Settings⚙️')]

# !!!!!  pages/fresh_dashboard_page.py !!!!!

pg = st.navigation(pages,position='sidebar')
pg.run()

