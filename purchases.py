import streamlit as st

#add purchase
def add_purchase():
    st.subheader("Add a purchase: ")

    item = st.text_input("What did you buy?")
    amount = st.number_input("How much did it cost?", min_value = 0.0, step = 1.0)
    purchase_date = st.date_input("When did you buy it?", value = None)

    categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
    category = st.selectbox("Select Category:", categories)

    if st.button("Add Purchase"):
        st.session_state.total_spent += amount
        st.session_state.transactions.append((item, amount, purchase_date, category))
        st.success("Purchase added!")

#purchase history
def purchase_history(): 
    st.subheader("Purchase History")

    if len(st.session_state.transactions) == 0:
        st.write("No purchases yet.")
    else:
        for item, amount, purchase_date, category in st.session_state.transactions:
            st.write(f"• {purchase_date} — {item} ({category}): -${amount:.2f}")

#reset
def reset_month():
    if st.button("Reset Month"):
        st.session_state.budget = 0.0
        st.session_state.total_spent = 0.0
        st.session_state.transactions = []

