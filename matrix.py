import streamlit as st 
import numpy as np 

st.set_page_config(page_title="Matrix Calculator", page_icon="🧮", layout="centered")

st.title("Smart Matrix Solver", text_alignment="center")

st.markdown("### Formula:")
st.latex(r"A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \ B = \begin{bmatrix} e & f \\ g & h \end{bmatrix}")


col1, col2 = st.columns(2)

try:
    with col1:
        st.markdown("### Matrix A:")
        a = st.number_input("Enter value of [a] :")
        b = st.number_input("Enter value of [b] :")
        c = st.number_input("Enter value of [c] :")
        d = st.number_input("Enter value of [d] :")
        
    with col2:
        st.markdown("### Matrix B:")
        e = st.number_input("Enter value of [e] :")
        f = st.number_input("Enter value of [f] :")
        g = st.number_input("Enter value of [g] :")
        h = st.number_input("Enter value of [h] :")

    st.divider()
        
    A = np.array([
        [a, b],
        [c, d]
    ])

    B = np.array([
        [e, f],
        [g, h]
    ])

    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("Addition", type="primary"):
            new = A + B
            st.markdown("### New Matrix:")
            st.write(new)
        
    with b2:
        if st.button("Subtraction", type="primary"):
            new = A - B
            st.markdown("### New Matrix:")
            st.write(new)
        
    with b3:
        if st.button("Matrix Multiplication", type="primary"):
            c11 = (a * e) + (b * g)
            c12 = (a * f) + (b * h)
            c21 = (c * e) + (d * g)
            c22 = (c * f) + (d * h)

            matrix_C = np.array([
                [c11, c12],
                [c21, c22]
            ])
            
            st.markdown("### New Matrix:")
            st.write(matrix_C)
            
    with b4:
        s = st.number_input("Enter Scalar Value:")
        if st.button("Scalar Multiplication", type="primary"):
            
            matrix1 = s*A 
            matrix2 = s*B
            
            
            st.markdown("### New Matrix:")
            st.write(matrix1)
            st.write()
            st.write(matrix2)
except Exception as e:
    st.error(e)