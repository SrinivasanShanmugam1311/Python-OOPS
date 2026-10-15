# ============================================================
# Project 01 : Bank Management System
# File        : models/savings_account.py
# Class       : SavingsAccount
# Purpose     : Savings account implementation
# ============================================================

from models.account import Account


class SavingsAccount(Account):
    """
    Represents a savings bank account.

    A savings account does not allow withdrawal beyond
    the available balance.
    """


    def withdraw(self, amount):
        """
        Withdraw money from a savings account.
        """

        # ----------------------------------------------------
        # Validate Amount
        # ----------------------------------------------------

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero"
            )


        # ----------------------------------------------------
        # Check Available Balance
        # ----------------------------------------------------

        if amount > self.get_balance():

            raise ValueError(
                "Insufficient balance"
            )


        # ----------------------------------------------------
        # Reduce Balance
        # ----------------------------------------------------

        self._reduce_balance(amount)

        print(
            "Savings account withdrawal successful"
        )