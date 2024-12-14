import streamlit as st

def print_percentage(salary, bill1, bill2, bill3):
    percentage = ((bill1 + bill2 + bill3) / salary) * 100
    st.write(f"Percentage of salary spent on bills: {int(percentage)}%")

st.title("Salary Bill Percentage Calculator")
st.info("Enter your salary and the amounts of 3 bills to calculate the percentage spent.")

salary = st.number_input("Enter your salary:", min_value=1, step=1)
bill1 = st.number_input("Enter the amount for bill 1:", min_value=0, step=1)
bill2 = st.number_input("Enter the amount for bill 2:", min_value=0, step=1)
bill3 = st.number_input("Enter the amount for bill 3:", min_value=0, step=1)

if st.button("Calculate Percentage"):
    if salary > 0:
        print_percentage(salary, bill1, bill2, bill3)
    else:
        st.error("Salary must be greater than zero.")