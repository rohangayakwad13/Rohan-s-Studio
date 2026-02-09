import streamlit as st 

st.set_page_config(page_title="Use tutorial",page_icon="🧑🏻‍🏫",layout="centered")
st.title("Use Tutorial")
st.subheader("How to use this web?.")
st.info("""✅ How To Use Rohan Studio

Yeh user ko step-by-step guide deta hai ki app kaise chalana hai.

🚀 How to Use Rohan Studio

Rohan Studio chalana bahut easy hai. Neeche har section ka use likha hua hai:

1️⃣ Standard Error (SE) Calculator

Do numbers enter karo

Calculate SE button dabao

Screen par Standard Error show ho jayega

2️⃣ Data Cleaner

Upload CSV file par file upload karo

Data preview dikh jayega

Select Columns se specific columns choose kar sakte ho

Remove NaN Rows par click karke missing data hata sakte ho

3️⃣ Calculator

Calculator tab me jaakar basic calculations kar sakte ho
(Addition, subtraction, multiplication, division)

4️⃣ SIP Calculator

Monthly investment, years, aur expected return bhar do

App automatically future amount calculate karega

5️⃣ Cramer's Rule (2 Variable)

2 equations ke coefficients enter karo

App x aur y ki values calculate karta hai

6️⃣ Cramer's Rule (3 Variable)

3 equations ke coefficients enter karo

x, y, z ki values step-by-step solve hoti hain

7️⃣ Quadratic Equation Solver

a, b, c ki values input karo

Roots (Real/Imaginary) calculate ho kar display honge

8️⃣ Matrix Solver

Matrix values enter karo

App determinant, transpose, inverse (agar possible ho) sab calculate karta hai

9️⃣ Factorization Formulas

Important algebraic formulas ek jagah list ki hui hain

Easy revision ke liye perfect section
""")
st.markdown("""
Agar aapko Rohan Studio ka koi feature samajhna ho, toh "How to Use" tab me step-by-step guidance di gayi hai.
Yeh guide aapko batayega ki kaun sa calculator kaise use karna hai, kis field me kya values enter karni hain, aur result kaise interpret karna hai.""")

st.markdown("------")
st.markdown("Creator : Rohan gayakwad", unsafe_allow_html=True)


if st.button("Main"):
    st.switch_page("main.py")
