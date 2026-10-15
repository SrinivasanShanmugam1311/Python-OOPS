# ============================================================
# Project 02 : Hospital Management System
# File        : models/bill.py
# Purpose     : Hospital billing model
# ============================================================

from dataclasses import dataclass


@dataclass
class Bill:
    """
    Represents a hospital bill.
    """

    bill_id: int
    patient_id: int
    amount: float
    description: str
    status: str = "Pending"

    def pay(self):
        """
        Mark the bill as paid.
        """

        self.status = "Paid"

    def display(self):
        """
        Display bill information.
        """

        print("=" * 50)
        print("HOSPITAL BILL")
        print("=" * 50)

        print("Bill ID     :", self.bill_id)
        print("Patient ID  :", self.patient_id)
        print("Amount      :", self.amount)
        print("Description :", self.description)
        print("Status      :", self.status)