# ============================================================
# Project 01 : Bank Management System
# File        : models/account.py
# Class       : Account
# Purpose     : Base class for bank accounts
# ============================================================

from abc import ABC, abstractmethod


class Account(ABC):
    """
    Abstract base class representing a bank account.

    Different account types such as:

        SavingsAccount
        CurrentAccount

    will inherit from this class.
    """

    def __init__(
        self,
        account_number,
        holder,
        balance=0
    ):
        """
        Create a bank account.

        Parameters:
            account_number : Unique account number
            holder         : Account holder
            balance        : Initial balance
        """

        self.account_number = account_number
        self.holder = holder

        # ----------------------------------------------------
        # Encapsulation
        # ----------------------------------------------------
        # Balance should not be changed directly from outside.
        #
        # Therefore we use a private variable.
        #
        # Python performs name mangling:
        #
        #     __balance
        #
        # becomes internally similar to:
        #
        #     _Account__balance
        # ----------------------------------------------------

        if balance < 0:
            raise ValueError(
                "Initial balance cannot be negative"
            )

        self.__balance = balance


    def deposit(self, amount):
        """
        Deposit money into the account.
        """

        # ----------------------------------------------------
        # Validation
        # ----------------------------------------------------

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero"
            )

        self.__balance += amount


    def get_balance(self):
        """
        Return the current account balance.

        We don't expose __balance directly.
        """

        return self.__balance


    def _reduce_balance(self, amount):
        """
        Reduce account balance.

        Protected method.

        This method is intended to be used by account
        subclasses such as SavingsAccount and CurrentAccount.
        """

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero"
            )

        self.__balance -= amount


    def withdraw(self, amount):
        """
        Withdraw money from the account.

        This method is abstract because different account
        types can have different withdrawal rules.
        """

        raise NotImplementedError


    def display_balance(self):
        """
        Display current balance.
        """

        print(
            f"Account {self.account_number} "
            f"Balance: {self.__balance}"
        )


    def __str__(self):
        """
        Return a readable account representation.
        """

        return (
            f"Account("
            f"number={self.account_number}, "
            f"holder='{self.holder}', "
            f"balance={self.__balance})"
        )