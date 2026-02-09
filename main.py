import streamlit as st 
import pandas as pd
import numpy as np
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Rohan Studio", page_icon="🤖", layout="centered")

col1, col2 = st.columns(2)

with col1:
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_py = load_lottiefile("Python logo.json")
    st_lottie(lottie_py, height=100)

with col2:
    st.title("Rohan's Studio")


# ---------------- SE CALCULATOR ----------------
st.header("Standard Error (SE) Calculator")
d1 = st.number_input("Enter Value 1")
d2 = st.number_input("Enter Value 2")

if st.button("Calculate SE"):
    data = [d1, d2]
    sd = np.std(data, ddof=1)
    se = sd / np.sqrt(len(data))
    
    st.success(f"Standard Error = {se}")

st.divider()

# ---------------- DATA CLEANER ----------------
st.header("Data Cleaner")
file = st.file_uploader("Upload CSV file", type="csv")

if file:
    try:
        df = pd.read_csv(file)
        st.write("Uploaded Data Preview")
        st.dataframe(df)

        col = st.multiselect("Select Columns", df.columns.tolist())
        if col:
            st.write("Filtered View")
            st.dataframe(df[col])

        if st.button("Remove NaN Rows"):
            df = df.dropna()
            st.success("NaN rows removed!")
            st.dataframe(df)

    except Exception as e:
        st.warning(str(e))

# ---------------- TABS ----------------
st.divider()
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Info", "Use", "Calculator", "SIP Calculator",
    "Cramer's Rule(2)", "Cramer's Rule(3)",
    "Quadratic Equation", "Matrix Solver", "Factorization Formulas"
])

with tab1:
    if st.button("Open Info Page", use_container_width=True):
        st.switch_page("pages/Info.py")

with tab2:
    if st.button("Open Use Page", use_container_width=True):
        st.switch_page("pages/use.py")

with tab3:
    if st.button("Open Calculator", use_container_width=True):
        st.switch_page("pages/project1.py")

with tab4:
    if st.button("Open SIP Calculator", use_container_width=True):
        st.switch_page("pages/sip_calc.py")

with tab5:
    if st.button("Open Cramer's Rule (2-Variable)", use_container_width=True):
        st.switch_page("pages/two_variable.py")

with tab6:
    if st.button("Open Cramer's Rule (3-Variable)", use_container_width=True):
        st.switch_page("pages/three_variable.py")

with tab7:
    if st.button("Open Quadratic Equation Solver", use_container_width=True):
        st.switch_page("pages/quadratic.py")

with tab8:
    if st.button("Open Matrix Solver", use_container_width=True):
        st.switch_page("pages/matrix.py")

with tab9:
    if st.button("Open Factorization Formulas", use_container_width=True):
        st.switch_page("pages/Factorization_Formulas.py")
        
st.feedback("stars")
