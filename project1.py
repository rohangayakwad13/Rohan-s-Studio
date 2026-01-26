import streamlit as st 

st.title("Rohan's calculator")
c = st.multiselect("Choose Here!", options=["Area Of Circle", "Simple Interest (SI)"])

if "Area Of Circle" in c:
    pi = 3.14
    radius = st.number_input("Enter Radius")
    total = pi * radius * radius
    st.write(f"Area OF Circle is {total}")

if "Simple Interest (SI)" in c:
    p = st.number_input("Enter Principal Amount")
    r = st.number_input("Enter Rate of Interest")
    t = st.number_input("Enter Tenure")
    total_si = (p * r * t) / 100
    st.write(f"Simple Interest (SI) is {total_si}")

if st.button("Main"):
    st.switch_page("main.py")