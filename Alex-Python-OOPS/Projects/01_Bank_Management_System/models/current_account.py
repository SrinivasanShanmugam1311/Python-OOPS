# ============================================================
# Project 01 : Bank Management System
# File        : models/current_account.py
# Class       : CurrentAccount
# Purpose     : Current account implementation
# ============================================================

from models.account import Account


class CurrentAccount(Account):
    """
    Represents a current account.

    A current account supports an overdraft facility.
    """

    # --------------------------------------------------------
    # Class Variable
    # --------------------------------------------------------
    # All CurrentAccount objects use this default overdraft
    # limit unless the value is changed at the class level.
    # --------------------------------------------------------

    overdraft_limit = 5000


    def withdraw(self, amount):
        """
        Withdraw money from a current account.

        Current accounts can use the overdraft facility.
        """

        # ----------------------------------------------------
        # Validate Amount
        # ----------------------------------------------------

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero"
            )


        # ----------------------------------------------------
        # Calculate Available Amount
        # ----------------------------------------------------
        # Example:
        #
        # Balance       = 2000
        # Overdraft     = 5000
        # Available     = 7000
        #
        # Therefore the customer can withdraw up to 7000.
        # ----------------------------------------------------

        available_amount = (
            self.get_balance()
            + self.overdraft_limit
        )


        # ----------------------------------------------------
        # Check Withdrawal Limit
        # ----------------------------------------------------

        if amount > available_amount:

            raise ValueError(
                "Withdrawal exceeds overdraft limit"
            )


        # ----------------------------------------------------
        # Reduce Balance
        # ----------------------------------------------------

        self._reduce_balance(amount)

        print(
            "Current account withdrawal successful"
        )