import streamlit as st 

st.set_page_config(page_title="Use tutorial",page_icon="🧑🏻‍🏫",layout="centered")
st.title("Use Tutorial")
st.subheader("How to use this web?.")
st.info("""How to use this web.
can you use this web easily.
this web create for biggnear.
""")
st.markdown("""
Agar aapko Rohan Studio ka koi feature samajhna ho, toh "How to Use" tab me step-by-step guidance di gayi hai.
Yeh guide aapko batayega ki kaun sa calculator kaise use karna hai, kis field me kya values enter karni hain, aur result kaise interpret karna hai.""")

st.markdown("------")
st.markdown("Creator : Rohan gayakwad", unsafe_allow_html=True)


if st.button("Main"):
    st.switch_page("main.py")