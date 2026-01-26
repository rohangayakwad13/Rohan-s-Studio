import streamlit as st 

st.set_page_config(page_title="SIP Calculator",page_icon="🛜", layout="centered")
st.title("SIP Caculator")
try:
    p = st.number_input("Enter Monthly SIP Amount")
    r = st.number_input("Enter Annual Interest rate (%)")
    t = int(st.number_input("Enter Tenuare"))

    i = r / 12 / 100
    fv = p * ((( (1+i)**(12*t) - 1 ))) / i 

    if st.button("Caculate"):
        st.markdown("Total SIP Calculation")
        st.write(fv)
        st.balloons()
        st.snow()
    with st.expander("Formula"):
        st.latex("FV = P x [(1 + r/n)^(nxt) - 1] / (r/n)")
        with st.expander("Formula in Code"):
            st.latex("FV = P * [(1 + r/n)**(n*t) - 1] / (r/n)")
    
    if st.button("Main"):
        st.switch_page("main.py")
     
except Exception:
    pass