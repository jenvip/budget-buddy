import streamlit as st

st.title("Budget Buddy 💸")

#backend 
if "budget" not in st.session_state:
    st.session_state.budget = 0.0

if "total_spent" not in st.session_state:
    st.session_state.total_spent = 0.0

if "transactions" not in st.session_state:
    st.session_state.transactions = []

#budget input
st.subheader("Input your monthly budget: ")
budget_input = st.number_input("Monthly Budget:", min_value = 0.0, step = 10.0)

if st.button("Save Budget"):
    st.session_state.budget = budget_input

#add purchase
st.subheader("Add a purchase: ")
item = st.text_input("What did you buy?")
amount = st.number_input("How much did it cost?", min_value = 0.0, step = 1.0)

if st.button("Add Purchase"):
    st.session_state.total_spent += amount
    st.session_state.transactions.append((item, amount))

#calculations
remaining = st.session_state.budget - st.session_state.total_spent
if st.session_state.budget > 0:
    percent_left = remaining / st.session_state.budget
else:
    percent_left = 0

#status
if percent_left > 0.5:
    status = "GREEN"
    color = "green"
elif percent_left > 0.2:
    status = "YELLOW"
    color = "yellow"
elif percent_left:
    status = "RED"
    color = "red"

st.markdown(
    f"<h3 style='color:{color}'>Status: {status}</h3>",
    unsafe_allow_html=True
)

#summary
st.subheader("Your Budget Summary")
st.metric("Total Spent", f"${st.session_state.total_spent:.2f}")
st.metric("Money Remaining", f"${remaining:.2f}")

#purchase history
st.subheader("Purchase History")
if len(st.session_state.transactions) == 0:
    st.write("No purchases yet.")
else:
    for item, amount in st.session_state.transactions:
        st.write(f"• {item}: -${amount:.2f}")

#reset
if st.button("Reset Month"):
    st.session_state.budget = 0.0
    st.session_state.total_spent = 0.0
    st.session_state.transactions = []

#background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #dce7dc;
    }
    </style>
    """,
    unsafe_allow_html=True
)
