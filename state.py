import streamlit as st
import pandas as pd
import os

DATA_FILE = "expense_history.csv"

def init_state():
    # Start with default values
    saved_transactions = []
    saved_budget = 0.0
    saved_spent = 0.0

    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        
        # Check if the file actually has data rows
        if not df.empty:
            # Convert the CSV rows back into Tuples
            saved_transactions = list(df[['Item', 'Amount', 'Date', 'Category']].itertuples(index=False, name=None))
            
            # Get the budget from the first row
            if 'Budget' in df.columns:
                saved_budget = float(df['Budget'].iloc[0])
            
            # Calculate total spent
            if 'Amount' in df.columns:
                saved_spent = df['Amount'].sum()
                
    if "budget" not in st.session_state:
        st.session_state.budget = saved_budget

    if "total_spent" not in st.session_state:
        st.session_state.total_spent = saved_spent

    if "transactions" not in st.session_state:
        st.session_state.transactions = saved_transactions

def save_to_csv():
    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions, columns=["Item", "Amount", "Date", "Category"])
    else:
        df = pd.DataFrame(columns=["Item", "Amount", "Date", "Category"])
    
    df['Budget'] = st.session_state.budget
    df.to_csv(DATA_FILE, index=False)
