import streamlit as st

def footer_home():
    st.markdown("""
    <div style="
        width:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        margin-top:30px;
    ">
        <p style="
            margin:0;
            font-weight:bold;
            color:black;
            text-align:center;
        ">
            Created with ❤️ by Rimanshu
        </p>
    </div>
    """, unsafe_allow_html=True)