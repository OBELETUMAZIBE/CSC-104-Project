import streamlit as st

# Base Account Class
class Account:
    def __init__(self, name, acc_type):
        self.name = name
        self.acc_type = acc_type
        self.balance = 0.0  # Initialize balance properly

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited into {self.acc_type} account."
        return "Enter a valid amount."

    def get_balance(self):
        return self.balance


# Savings Account with withdrawal limit
class SavingsAccount(Account):
    def __init__(self, name):
        super().__init__(name, "savings")
        self.withdrawal_limit = 5000

    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.withdrawal_limit:
            self.balance -= amount
            return f"{amount} withdrawn from savings account."
        return "Withdrawal exceeds limit or insufficient funds."


# Current Account with no limit
class CurrentAccount(Account):
    def __init__(self, name):
        super().__init__(name, "current")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn from current account."
        return "Insufficient funds."


# Streamlit App Logic
st.title("Simple Banking App")

# Store account in session_state to persist data
if 'account' not in st.session_state:
    st.session_state.account = None

account_type = st.selectbox("Choose Account Type", ["Savings", "Current"])
name = st.text_input("Enter Account Holder Name")

# Show an info message before account is created
if st.session_state.account is None:
    st.info("Please create an account to begin.")

if st.button("Create Account"):
    if name:
        if account_type == "Savings":
            st.session_state.account = SavingsAccount(name)
        else:
            st.session_state.account = CurrentAccount(name)
        st.success(f"✅ Account created for {name} ({account_type})")
    else:
        st.error("⚠️ Please enter a name to create an account.")

if st.session_state.account:
    st.subheader(f"👋 Welcome, {st.session_state.account.name}")

    # Show withdrawal limit notice for savings account
    if isinstance(st.session_state.account, SavingsAccount):
        st.caption("⛔ Note: Withdrawal limit per transaction is ₦5000.")

    amount = st.number_input("Enter Amount", min_value=0.0, step=1.0)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Deposit"):
            st.write(st.session_state.account.deposit(amount))
    with col2:
        if st.button("Withdraw"):
            st.write(st.session_state.account.withdraw(amount))

    st.info(f"💰 Current Balance: ₦{st.session_state.account.get_balance():,.2f}")
