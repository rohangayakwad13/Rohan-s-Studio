import streamlit as st 

st.set_page_config(page_title="Cramer's Rule 3 Variable", page_icon="👩🏻‍💻")
# Formula: a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

st.title("Cramer's Rule (3 Variable)")

st.latex(r"a_1x + b_1y + c_1z = d_1")
st.latex(r"a_2x + b_2y + c_2z = d_2")
st.latex(r"a_3x + b_3y + c_3z = d_3")


col1, col2, col3, col4 = st.columns(4)

with col1:
    a1 = st.number_input("Enter a1 Value")
    a2 = st.number_input("Enter a2 Value")
    a3 = st.number_input("Enter a3 Value")
    
with col2:
    b1 = st.number_input("Enter b1 Value")
    b2 = st.number_input("Enter b2 Value")
    b3 = st.number_input("Enter b3 Value")
    
with col3:
    c1 = st.number_input("Enter c1 Value")
    c2 = st.number_input("Enter c2 Value")
    c3 = st.number_input("Enter c3 Value")
    

with col4:
    d1 = st.number_input("Enter d1 Value")
    d2 = st.number_input("Enter d2 Value")
    d3 = st.number_input("Enter d3 Value")
    
if st.button("Calculate", type="primary"):
    
    a, b, c = a1, b1, c1
    d, e, f = a2, b2, c2 
    g, h, i = a3, b3, c3
    
    a2, b2, c2 = d1, d1, d1
    d2, e2, f2 = d2, d2, d2 
    g2, h2, i2 = d3, d3, d3
    
    D = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    
    if D == 0:
        st.error("No❌ Unique Solution! (D = 0)")
        
    else:

        Dx = a2*(e*i-f*h)-b*(d2*i-f*g2)+c*(d2*h-e*g2)
        Dy = a*(e2*i-f*h2)-b2*(d*i-f*g)+c*(d*h2-e2*g)
        Dz = a*(e*i2-f2*h)-b*(d*i2-f2*g)+c2*(d*h-e*g)
    
        x = Dx / D
        y = Dy / D 
        z = Dz / D 
        
        st.metric("Value of x", x)
        st.metric("Value of y", y)
        st.metric("Value of z", z)
        
        st.snow()
        st.balloons()