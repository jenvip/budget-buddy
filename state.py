import streamlit as st

def init_state():
    if "budget" not in st.session_state:
        st.session_state.budget = 0.0

    if "total_spent" not in st.session_state:
        st.session_state.total_spent = 0.0

    if "transactions" not in st.session_state:
        st.session_state.transactions = []


