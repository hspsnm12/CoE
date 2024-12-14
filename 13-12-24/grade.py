import streamlit as st
def grade(project, internal, external):
    if project >= 50 and internal >= 50 and external >= 50:
        project = project * 0.70
        internal = internal * 0.10
        external = external * 0.20
        total_marks = project + internal + external
        if total_marks > 90:
            st.success("'A' grade")
        elif 80 < total_marks <= 90:
            st.success("'B' grade")
        else:
            st.success("'C' grade")
    else:
        if project < 50:
            st.error(f"Failed in project, score: {project}")
        if internal < 50:
            st.error(f"Failed in internal, score: {internal}")
        if external < 50:
            st.error(f"Failed in external, score: {external}")

st.title("Grade Calculation")
st.info("Your performance:")
project = st.number_input("Enter the marks in project:", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter the marks in internal:", min_value=0, max_value=100, step=1)
external = st.number_input("Enter the marks in external:", min_value=0, max_value=100, step=1)

if st.button("Calculate Grade"):
    grade(project, internal, external)