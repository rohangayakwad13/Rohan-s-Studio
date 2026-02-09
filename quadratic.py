import streamlit as st 
import cmath as m

st.set_page_config(page_title="Quadratic Equation Solver", page_icon="🤖", layout="centered")
st.title("Quadratic Equation Solver")

st.markdown("### Formula:")
st.latex(r"Ax^2 + Bx + C = 0")

st.markdown("### Discriminant:")
st.latex(r"D = B^2 - 4AC")

a = st.number_input("Enter A Value")
b = st.number_input("Enter B Value")
c = st.number_input("Enter C Value")

D = b**2 - 4*a*c 
dsqr = m.sqrt(D)



if st.button("Calculate", type="primary"):
    if D > 0:
        x1 = (-b + dsqr) / (2*a)
        x2 = (-b - dsqr) / (2*a)

        st.metric("Value of x1", x1)
        st.metric("Value of x2", x2)
        st.write("2 real Roots")
        st.success(D)
        
    elif D == 0:
        x = -b / (2*a)
        st.metric("Value of x", x)
        st.write("real Root")
        st.success(D)
        
    elif D < 0:
        x1 = (-b + dsqr) / (2*a)
        x2 = (-b - dsqr) / (2*a)
        
        st.metric("Value of x1", x1)
        st.metric("Value of x2", x2)    
        
        st.write("Complex Root")
        st.success(D)
        
    st.balloons()