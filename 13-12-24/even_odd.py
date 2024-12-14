import streamlit as st
st.title("EVEN OR ODD")
num1 = st.number_input("Enter number",min_value=1,step=1)
if st.button("Even/Odd"):
    if num1%2==0:
        st.success("Even number")
    else:
        st.error("Odd number")

