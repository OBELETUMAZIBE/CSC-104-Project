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
