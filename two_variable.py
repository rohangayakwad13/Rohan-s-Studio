import streamlit as st
import numpy as np

st.title("Cramer's Rule Calculator (2 Variables)")

st.subheader("Equations:")
st.latex(r"a_1x + b_1y = c_1")
st.latex(r"a_2x + b_2y = c_2")

st.subheader("Formulas:")
st.markdown("### Determinants:")
st.latex(r"D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1b_2 - a_2b_1")
st.latex(r"D_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} = c_1b_2 - c_2b_1")
st.latex(r"D_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} = a_1c_2 - a_2c_1")

st.subheader("Enter Values:")

col1, col2 = st.columns(2)
with col1:
    a1 = st.number_input("Enter a1")
    b1 = st.number_input("Enter b1")
    c1 = st.number_input("Enter c1")

with col2:
    a2 = st.number_input("Enter a2")
    b2 = st.number_input("Enter b2")
    c2 = st.number_input("Enter c2")

if st.button("Calculate", type="primary"):
    D = (a1 * b2) - (a2 * b1)
    Dx = (c1 * b2) - (c2 * b1)
    Dy = (a1 * c2) - (a2 * c1)

    st.write("### Results:")

    st.write(f"**D  = {D}**")
    st.write(f"**Dx = {Dx}**")
    st.write(f"**Dy = {Dy}**")

    if D == 0:
        st.error("❌ No Unique Solution (D = 0)")
    else:
        x = Dx / D
        y = Dy / D

        st.metric("Value of x", x)
        st.metric("Value of y", y)
