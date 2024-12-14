import streamlit as st
st.title("Gross Salary Calculator")
basic = st.number_input("Enter your basic salary:",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
    hra = 0
    da = 0
    if basic < 10000:
        hra = basic * 0.67
        da = basic * 0.73
    elif 10000 <= basic <= 20000:
        hra = basic * 0.69
        da = basic * 0.76
    else:
        hra = basic * 0.73
        da = basic * 0.89
    gs = hra + da + basic
    st.success(gs)