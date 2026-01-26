import streamlit as st 

st.set_page_config(page_title="Rohan Studio", page_icon="🤖", layout="centered")
st.title("Rohan Studio")

tab1, tab2, tab3, tab4 = st.tabs(["Info", "Use", "Calculator", "SIP Calculator"])
with tab1:
    if st.button("Info", type="secondary", use_container_width=True):
        st.switch_page("pages/Info.py")
        
with tab2:
    if st.button("Calculator", type="primary", use_container_width=True):
        st.switch_page("pages/project1.py")
        
with tab3:
    if st.button("Use", type="tertiary", use_container_width=True):
        st.switch_page("pages/use.py")

with tab4:
    if st.button("SIP Calculator"):
        st.switch_page("pages/sip_calc.py")

st.feedback("stars")