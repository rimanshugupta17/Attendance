import streamlit as st
def header_home():
    logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnOQhoq-DfpTLOWrQmHKVAnROVj5Mg09oECTgf60D1dQ&s=10'
    st.markdown(f"""
    <div  style="display:flex; flex-direction:column ; align-item:center; justify-content:center; margin-bottom:30px">         
        <img src='{logo_url}' style='height:100px'; />
        <h1 style='text-align:center; color:#E03FF'> AttendIQ </h1>
    </div>

 """,unsafe_allow_html=True)
    
def header_dashboard():
    logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnOQhoq-DfpTLOWrQmHKVAnROVj5Mg09oECTgf60D1dQ&s=10'
    st.markdown(f"""
    <div  style="display:flex; align-items:center; justify-content:center; gap:10px">         
        <img src='{logo_url}' style='height:85px;'/>
        <h2 style='text-align:center; color:#C93112 !important'> AttendIQ </h2>
    </div>

 """,unsafe_allow_html=True)