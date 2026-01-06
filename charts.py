import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

#pie chart of spending by category
def pie_chart():
    st.subheader("Spending Distribution Among Categories")

    if not st.session_state.transactions:
        st.info("No transactions yet to display.")
        return

    df = pd.DataFrame(
        st.session_state.transactions,
        columns=["Item", "Amount", "Date", "Category"]
    )

    category_sums = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(
        category_sums,
        labels=category_sums.index,
        autopct="%1.1f%%",
        startangle=140
    )
    ax.axis("equal")

    st.pyplot(fig)

#bar chart of planned budget vs actual spending 
def bar_chart():
    st.subheader("Planned Budget vs Actual Spending")

    budget = st.session_state.budget
    spent = st.session_state.total_spent

    if budget == 0:
        st.info("Please set a budget to view this chart.")
        return

    fig, ax = plt.subplots()
    ax.bar(
        ["Planned Budget", "Actual Spending"],
        [budget, spent]
    )

    ax.set_ylabel("Amount ($)")
    ax.set_title("Budget vs Spending")

    st.pyplot(fig)