# ============================================================
# Project 01 : Bank Management System
# File        : models/transaction.py
# Class       : Transaction
# Purpose     : Represents a banking transaction
# ============================================================

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    """
    Represents one banking transaction.

    Dataclass automatically provides useful methods such as:

        __init__()
        __repr__()
        __eq__()

    """

    transaction_id: int
    transaction_type: str
    amount: float
    account_number: int
    timestamp: datetime


    def display(self):
        """
        Display transaction information.
        """

        print()
        print("----------------------------------------")
        print("Transaction ID :", self.transaction_id)
        print("Type           :", self.transaction_type)
        print("Amount         :", self.amount)
        print("Account        :", self.account_number)
        print("Date           :", self.timestamp)
        print("----------------------------------------")