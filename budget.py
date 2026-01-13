import streamlit as st
from state import save_to_csv

#budget input
def budget_input():
    st.subheader("Input your monthly budget: ")
    budget_input = st.number_input("Monthly Budget:", min_value = 0.0, step = 10.0)

    if st.button("Save Budget"):
        st.session_state.budget = budget_input
        save_to_csv()
        st.success("Budget saved!")

#budget status
def budget_status():
    remaining = st.session_state.budget - st.session_state.total_spent
    if st.session_state.budget > 0:
        percent_left = remaining / st.session_state.budget
    else:
        percent_left = 0

    if percent_left > 0.5:
        status = "GREEN"
        color = "green"
    elif percent_left > 0.2:
        status = "YELLOW"
        color = "yellow"
    else:
        status = "RED"
        color = "red"

    st.markdown(
        f"<h3 style='color:{color}'>Status: {status}</h3>",
        unsafe_allow_html=True
    )

    st.subheader("Budget Summary: ")
    st.metric("Total Spent", f"${st.session_state.total_spent:.2f}")
    st.metric("Money Remaining", f"${remaining:.2f}")
