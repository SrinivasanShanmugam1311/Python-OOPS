# ============================================================
# Project 01 : Bank Management System
# File        : main.py
# Purpose     : Application Entry Point + Menu
# Level       : Intermediate → Advanced
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

# ------------------------------------------------------------
# BankService
# ------------------------------------------------------------
# BankService contains the actual banking business logic.
#
# main.py should mainly:
#
#     1. Display menu
#     2. Read user input
#     3. Call BankService methods
#     4. Display results
#
# Business logic should remain inside BankService.
# ------------------------------------------------------------

from services.bank_service import BankService


# ------------------------------------------------------------
# Custom Banking Exception
# ------------------------------------------------------------
# BankError is the parent exception for our banking-specific
# errors.
#
# We can catch it in one place.
# ------------------------------------------------------------

from exceptions.bank_exceptions import BankError


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():
    """
    Display the main application menu.
    """

    print()
    print("=" * 60)
    print("              BANK MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Create Customer")
    print("2. Create Savings Account")
    print("3. Create Current Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Balance")
    print("7. View Customers")
    print("8. View Accounts")
    print("9. View Transactions")
    print("0. Exit")

    print("=" * 60)


# ============================================================
# CREATE CUSTOMER
# ============================================================

def create_customer(bank):
    """
    Read customer information and create a new customer.
    """

    print()
    print("----- CREATE CUSTOMER -----")

    name = input("Enter customer name : ")
    email = input("Enter customer email: ")

    customer = bank.create_customer(
        name=name,
        email=email
    )

    print()
    print("Customer created successfully.")
    print("Customer ID :", customer.customer_id)
    print("Name        :", customer.name)
    print("Email       :", customer.email)


# ============================================================
# CREATE SAVINGS ACCOUNT
# ============================================================

def create_savings_account(bank):
    """
    Create a savings account for an existing customer.
    """

    print()
    print("----- CREATE SAVINGS ACCOUNT -----")

    customer_id = int(
        input("Enter customer ID   : ")
    )

    initial_balance = float(
        input("Enter initial balance: ")
    )

    account = bank.create_savings_account(
        customer_id=customer_id,
        initial_balance=initial_balance
    )

    print()
    print("Savings account created successfully.")
    print(
        "Account Number :",
        account.account_number
    )

    print(
        "Holder         :",
        account.holder
    )

    print(
        "Balance        :",
        account.get_balance()
    )


# ============================================================
# CREATE CURRENT ACCOUNT
# ============================================================

def create_current_account(bank):
    """
    Create a current account for an existing customer.
    """

    print()
    print("----- CREATE CURRENT ACCOUNT -----")

    customer_id = int(
        input("Enter customer ID   : ")
    )

    initial_balance = float(
        input("Enter initial balance: ")
    )

    account = bank.create_current_account(
        customer_id=customer_id,
        initial_balance=initial_balance
    )

    print()
    print("Current account created successfully.")

    print(
        "Account Number :",
        account.account_number
    )

    print(
        "Holder         :",
        account.holder
    )

    print(
        "Balance        :",
        account.get_balance()
    )


# ============================================================
# DEPOSIT
# ============================================================

def deposit_money(bank):
    """
    Deposit money into an account.
    """

    print()
    print("----- DEPOSIT MONEY -----")

    account_number = int(
        input("Enter account number: ")
    )

    amount = float(
        input("Enter deposit amount: ")
    )

    bank.deposit(
        account_number,
        amount
    )

    print()
    print("Deposit successful.")

    print(
        "New Balance:",
        bank.get_balance(account_number)
    )


# ============================================================
# WITHDRAW
# ============================================================

def withdraw_money(bank):
    """
    Withdraw money from an account.
    """

    print()
    print("----- WITHDRAW MONEY -----")

    account_number = int(
        input("Enter account number : ")
    )

    amount = float(
        input("Enter withdrawal amount: ")
    )

    bank.withdraw(
        account_number,
        amount
    )

    print()
    print("Withdrawal successful.")

    print(
        "New Balance:",
        bank.get_balance(account_number)
    )


# ============================================================
# CHECK BALANCE
# ============================================================

def check_balance(bank):
    """
    Display the balance of an account.
    """

    print()
    print("----- CHECK BALANCE -----")

    account_number = int(
        input("Enter account number: ")
    )

    balance = bank.get_balance(
        account_number
    )

    print()
    print("Account Number:", account_number)
    print("Balance       :", balance)


# ============================================================
# VIEW CUSTOMERS
# ============================================================

def view_customers(bank):
    """
    Display all customers.
    """

    bank.display_customers()


# ============================================================
# VIEW ACCOUNTS
# ============================================================

def view_accounts(bank):
    """
    Display all accounts.
    """

    bank.display_accounts()


# ============================================================
# VIEW TRANSACTIONS
# ============================================================

def view_transactions(bank):
    """
    Display transaction history for an account.
    """

    print()
    print("----- TRANSACTION HISTORY -----")

    account_number = int(
        input("Enter account number: ")
    )

    bank.display_transactions(
        account_number
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():
    """
    Start and control the Bank Management System.
    """

    # --------------------------------------------------------
    # Create one BankService object.
    # --------------------------------------------------------
    # This object will maintain:
    #
    #     customers
    #     accounts
    #     transactions
    #
    # throughout the application session.
    # --------------------------------------------------------

    bank = BankService()


    print()
    print("=" * 60)
    print("          WELCOME TO BANK MANAGEMENT SYSTEM")
    print("=" * 60)


    # ========================================================
    # APPLICATION LOOP
    # ========================================================
    # The menu continues until the user selects 0.
    # ========================================================

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()


        # ====================================================
        # CREATE CUSTOMER
        # ====================================================

        if choice == "1":

            try:
                create_customer(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # CREATE SAVINGS ACCOUNT
        # ====================================================

        elif choice == "2":

            try:
                create_savings_account(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # CREATE CURRENT ACCOUNT
        # ====================================================

        elif choice == "3":

            try:
                create_current_account(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # DEPOSIT
        # ====================================================

        elif choice == "4":

            try:
                deposit_money(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # WITHDRAW
        # ====================================================

        elif choice == "5":

            try:
                withdraw_money(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # CHECK BALANCE
        # ====================================================

        elif choice == "6":

            try:
                check_balance(bank)

            except BankError as error:

                print()
                print("Bank Error:", error)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # VIEW CUSTOMERS
        # ====================================================

        elif choice == "7":

            try:
                view_customers(bank)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # VIEW ACCOUNTS
        # ====================================================

        elif choice == "8":

            try:
                view_accounts(bank)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # VIEW TRANSACTIONS
        # ====================================================

        elif choice == "9":

            try:
                view_transactions(bank)

            except Exception as error:

                print()
                print("Error:", error)


        # ====================================================
        # EXIT
        # ====================================================

        elif choice == "0":

            print()
            print("=" * 60)
            print("Thank you for using Bank Management System.")
            print("Goodbye!")
            print("=" * 60)

            break


        # ====================================================
        # INVALID MENU OPTION
        # ====================================================

        else:

            print()
            print(
                "Invalid choice. "
                "Please select a valid option."
            )


# ============================================================
# PYTHON ENTRY POINT
# ============================================================
# When we run:
#
#     python main.py
#
# Python sets:
#
#     __name__ = "__main__"
#
# and main() is executed.
#
# If another file imports main.py, main() will not
# automatically execute.
# ============================================================

if __name__ == "__main__":
    main()