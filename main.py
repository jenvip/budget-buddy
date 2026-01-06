import streamlit as st
from purchases import add_purchase, purchase_history, reset_month
from budget import budget_input, budget_status
from state import init_state
from styles import styles
from charts import pie_chart, bar_chart

st.title("Budget Buddy 💸")

styles()
init_state()
budget_input()
add_purchase()
budget_status()
purchase_history()
reset_month()
pie_chart()
bar_chart()
