import streamlit as st

def style_base_layout():
    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800;900&display=swap');
                .block-container{
                    padding-top:1.5rem !important
                }
                h1{
                font-family:'League Spartan',sans-serif !important;
                    font-size:3.0rem !important;
                    color:white !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                }
                h2{
                    font-family:'League Spartan',sans-serif !important;
                    font-size:2rem !important;
                    color:black !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                }
                h3,h4,p{
                    font-family:'League Spartan',sans-serif !important;  
                }
                button{
                    border-radius:1.5rem !important;
                    background:black !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border:none !important;
                    transition :transform 0.25s ease-in-out !important;
                }
                button[kind="secondary"]{
                    border-radius:1.5rem !important;
                    background:#5865F2 !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border:none !important;
                    transition :transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    background-color:#EB459E !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border:none !important;
                    transition :transform 0.25s ease-in-out !important;
                }
                button:hover{
                    transform :scale(1.05)
                }
        </style>

    """,unsafe_allow_html=True)

def style_background_home():
    st.markdown("""
        <style>
            .stApp{
                background: #FFA2A2 !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius:5rem !important;
            }
        </style>

    """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background:#FFA2A2 !important;
            }
        </style>

    """,unsafe_allow_html=True)