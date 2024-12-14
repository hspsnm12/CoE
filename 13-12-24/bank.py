import streamlit as st
class Bank:
    acbal = 10000
    transaction = 0
    def validation(self, user_pin):
        pin = 1234
        return user_pin == pin
    def viewOptions(self):
        st.success("1. Deposit\n2. Withdraw\n3. Bal Enquiry\n0. EXIT\nChoose an option:")
    def performAction(self, inp):
        if inp == 1:
            depo = st.number_input("Enter amount to be deposited:", key="deposit_amount")
            self.deposit(depo)
        elif inp == 2:
            withdraw = st.number_input("Enter the amount to be withdrawn:", key="withdraw_amount")
            self.amt_withdraw(withdraw)
        elif inp == 3:
            st.info(f"Your current balance is: {self.acbal}")
        elif inp == 0:
            st.info("EXIT")
        else:
            st.error("Invalid option.")
    def deposit(self, depo):
        if depo % 100 == 0 and depo <= 50000:
            self.acbal += depo
            st.success(f"Transaction successful. Your new balance is: {self.acbal}")
        else:
            st.error("Transaction failed.")
            if depo % 100 != 0:
                st.warning("Amount should be a multiple of 100.")
            if depo > 50000:
                st.warning("Max deposit amount is 50K.")
    def amt_withdraw(self, withdraw):
        if (withdraw >= 100 and withdraw % 100 == 0 and withdraw < self.acbal and self.acbal - withdraw > 500 and withdraw <= 20000 and self.transaction < 3):
            self.acbal -= withdraw
            st.success(f"Transaction successful. Your new balance is: {self.acbal}")
            self.transaction += 1
        else:
            st.error("Transaction failed.")
            if withdraw % 100 != 0:
                st.warning("Amount should be a multiple of 100.")
            if withdraw > self.acbal:
                st.warning("Withdraw amount should be less than the account balance.")
            if self.acbal - withdraw < 500:
                st.warning("Minimum balance should be 500.")
            if withdraw > 20000:
                st.warning("Per transaction, 20K is the max withdrawal amount.")
            if self.transaction >= 3:
                st.warning("Only 3 transactions allowed per day.")
st.title("Welcome to ABC Bank")
obj = Bank()
pin_attempts = 0
max_attempts = 3
pin_valid = False
user_pin = st.text_input("Enter your PIN:", type="password", key="pin_input")
if user_pin:
    while pin_attempts < max_attempts and not pin_valid:
        try:
            if obj.validation(int(user_pin)):
                st.success("Pin validated successfully.")
                pin_valid = True
            else:
                pin_attempts += 1
                if pin_attempts < max_attempts:
                    st.error(f"Incorrect PIN. Attempt {pin_attempts + 1} of {max_attempts}. Try again.")
                    user_pin = st.text_input("Enter your PIN:", type="password", key=f"pin_input_{pin_attempts}")
                else:
                    st.error("Incorrect PIN. You have reached the maximum attempts limit.")
        except ValueError:
            st.error("Please enter a valid PIN.")
            break
if pin_valid:
    selected_option = st.selectbox("Choose an option:", ["Deposit", "Withdraw", "Balance Enquiry", "Exit"], key="menu_option")

    if selected_option == "Deposit":
        obj.performAction(1)
    elif selected_option == "Withdraw":
        obj.performAction(2)
    elif selected_option == "Balance Enquiry":
        obj.performAction(3)
    elif selected_option == "Exit":
        obj.performAction(0)
else:
    st.error("Access Denied. Please try again later.")