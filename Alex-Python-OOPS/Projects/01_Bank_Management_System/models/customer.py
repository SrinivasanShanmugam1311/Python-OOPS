# ============================================================
# Project 01 : Bank Management System
# File        : models/customer.py
# Class       : Customer
# Purpose     : Represents a bank customer
# ============================================================


class Customer:
    """
    Represents a customer of the bank.

    A customer can own one or more bank accounts.
    """

    def __init__(self, customer_id, name, email):
        """
        Create a new Customer object.

        Parameters:
            customer_id : Unique customer identifier
            name        : Customer name
            email       : Customer email address
        """

        # ----------------------------------------------------
        # Customer Information
        # ----------------------------------------------------
        self.customer_id = customer_id
        self.name = name
        self.email = email

        # ----------------------------------------------------
        # Account Collection
        # ----------------------------------------------------
        # A customer can have multiple accounts.
        #
        # Example:
        #
        # Customer
        #     |
        #     +-- Savings Account
        #     |
        #     +-- Current Account
        #
        # This demonstrates COMPOSITION / HAS-A relationship.
        # ----------------------------------------------------

        self.accounts = []


    def add_account(self, account):
        """
        Add an account to the customer's account list.
        """

        self.accounts.append(account)


    def remove_account(self, account):
        """
        Remove an account from the customer's account list.
        """

        if account in self.accounts:
            self.accounts.remove(account)


    def get_accounts(self):
        """
        Return all accounts owned by the customer.
        """

        return self.accounts


    def display_details(self):
        """
        Display customer information.
        """

        print()
        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)
        print("Email       :", self.email)

        print("Accounts    :", len(self.accounts))


    def __str__(self):
        """
        Return a readable representation of the customer.
        """

        return (
            f"Customer("
            f"id={self.customer_id}, "
            f"name='{self.name}', "
            f"email='{self.email}')"
        )