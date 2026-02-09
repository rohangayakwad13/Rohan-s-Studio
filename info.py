import streamlit as st 

st.set_page_config(page_title="Studio Info", page_icon="ℹ️", layout="centered")
st.title("INFO of this Rohan Studio web")
st.info("""✅ Rohan Studio Info

Yeh bataata hai ki app kya karta hai aur kaise banaya hai.

ℹ️ About Rohan Studio

Rohan Studio ek multipurpose learning application hai jo mathematics aur data-processing tools ko ek hi jagah par provide karta hai.
Ye app Streamlit, Python, NumPy, Pandas aur Lottie Animations ka use karke banaya gaya hai.

Is app ka main goal hai students ko simple aur interactive way me important formulas aur tools sikhana.

🧩 Features

Standard Error (SE) Calculator
Do values ke basis par standard error calculate karta hai.

Data Cleaner
CSV file upload karke
✔ Missing values (NaN) remove kar sakte ho
✔ Specific columns select karke filtered data dekh sakte ho

General Calculator
Normal mathematical calculations ke liye.

SIP Calculator
Monthly investment ka future value calculate karta hai.

Cramer's Rule (2 & 3 variables)
Linear equations solve karta hai step-by-step.

Quadratic Equation Solver
a, b, c ke basis par roots find karta hai.

Matrix Solver
2×2 aur 3×3 matrices solve karne ka tool.

Factorization Formulas
Important math formulas ek jagah par.

🎯 Purpose

Students ko important maths topics practical way me sikhana

Coding + Mathematics dono ek platform me provide karna

Streamlit ka real-world use dikhana""")

if st.button("Main"):
    st.switch_page("main.py")
