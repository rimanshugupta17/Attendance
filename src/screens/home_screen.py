import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.style_base_layout import style_base_layout,style_background_home
def home_screen():


    style_base_layout()

    header_home()
    style_background_home()
    col1,col2=st.columns(2,gap='large')
    with col1:
           st.header("Student Portal")
           st.image("https://media.istockphoto.com/id/1444077739/photo/college-study-and-education-student-man-portrait-with-back-to-school-backpack-and-portfolio.jpg?s=612x612&w=0&k=20&c=PAQmqKzYd3OiKhlfrT1DVMQNkGu-drX4rtJ5p6y7D8c=",width=120)
           if st.button('student portal'):
                 st.session_state['login_type']='student'
                 st.rerun()
    with col2:
           st.header("Teacher Portal")
           st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCZsUs4eABq-huGiPIV9fGUmASROLUpx0D8y_Br5YkYQ&s=10",width=120)
           if st.button('teacher portal'):
                 st.session_state['login_type']='teacher'        
                 st.rerun()
    footer_home()