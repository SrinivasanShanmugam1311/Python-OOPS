# ============================================================
# Project 01 : Bank Management System
# File        : tests/test_transaction.py
# Purpose     : Test Transaction class
# Testing     : unittest
# ============================================================


# ------------------------------------------------------------
# Import unittest
# ------------------------------------------------------------

import unittest


# ------------------------------------------------------------
# Import Transaction
# ------------------------------------------------------------

from models.transaction import Transaction


# ------------------------------------------------------------
# Import datetime
# ------------------------------------------------------------

from datetime import datetime


# ============================================================
# TRANSACTION TEST CLASS
# ============================================================

class TestTransaction(unittest.TestCase):
    """
    Test cases for the Transaction dataclass.
    """


    # ========================================================
    # TEST TRANSACTION CREATION
    # ========================================================

    def test_transaction_creation(self):
        """
        Verify that a Transaction object is created correctly.
        """

        transaction_time = datetime.now()

        transaction = Transaction(
            transaction_id=1,
            transaction_type="DEPOSIT",
            amount=5000,
            account_number=1001,
            timestamp=transaction_time
        )

        # ----------------------------------------------------
        # Verify Transaction ID
        # ----------------------------------------------------

        self.assertEqual(
            transaction.transaction_id,
            1
        )

        # ----------------------------------------------------
        # Verify Transaction Type
        # ----------------------------------------------------

        self.assertEqual(
            transaction.transaction_type,
            "DEPOSIT"
        )

        # ----------------------------------------------------
        # Verify Amount
        # ----------------------------------------------------

        self.assertEqual(
            transaction.amount,
            5000
        )

        # ----------------------------------------------------
        # Verify Account Number
        # ----------------------------------------------------

        self.assertEqual(
            transaction.account_number,
            1001
        )

        # ----------------------------------------------------
        # Verify Timestamp
        # ----------------------------------------------------

        self.assertEqual(
            transaction.timestamp,
            transaction_time
        )


    # ========================================================
    # TEST WITHDRAWAL TRANSACTION
    # ========================================================

    def test_withdrawal_transaction(self):
        """
        Verify that a withdrawal transaction can be created.
        """

        transaction = Transaction(
            transaction_id=2,
            transaction_type="WITHDRAW",
            amount=1000,
            account_number=1002,
            timestamp=datetime.now()
        )

        self.assertEqual(
            transaction.transaction_type,
            "WITHDRAW"
        )

        self.assertEqual(
            transaction.amount,
            1000
        )


    # ========================================================
    # TEST DATACLASS REPRESENTATION
    # ========================================================

    def test_transaction_repr(self):
        """
        Dataclass automatically provides __repr__().
        """

        transaction = Transaction(
            transaction_id=3,
            transaction_type="DEPOSIT",
            amount=2500,
            account_number=1003,
            timestamp=datetime.now()
        )

        result = repr(transaction)

        # ----------------------------------------------------
        # The generated representation should contain useful
        # information about the object.
        # ----------------------------------------------------

        self.assertIn(
            "Transaction",
            result
        )

        self.assertIn(
            "2500",
            result
        )

        self.assertIn(
            "1003",
            result
        )


    # ========================================================
    # TEST DATACLASS EQUALITY
    # ========================================================

    def test_transaction_equality(self):
        """
        Dataclass automatically provides value-based equality.

        Two Transaction objects containing the same values
        should compare as equal.
        """

        transaction_time = datetime.now()

        transaction1 = Transaction(
            transaction_id=4,
            transaction_type="DEPOSIT",
            amount=1000,
            account_number=1004,
            timestamp=transaction_time
        )

        transaction2 = Transaction(
            transaction_id=4,
            transaction_type="DEPOSIT",
            amount=1000,
            account_number=1004,
            timestamp=transaction_time
        )

        self.assertEqual(
            transaction1,
            transaction2
        )


    # ========================================================
    # TEST TRANSACTION INEQUALITY
    # ========================================================

    def test_transaction_inequality(self):
        """
        Transactions with different values should not be equal.
        """

        transaction1 = Transaction(
            transaction_id=5,
            transaction_type="DEPOSIT",
            amount=1000,
            account_number=1005,
            timestamp=datetime.now()
        )

        transaction2 = Transaction(
            transaction_id=6,
            transaction_type="WITHDRAW",
            amount=500,
            account_number=1005,
            timestamp=datetime.now()
        )

        self.assertNotEqual(
            transaction1,
            transaction2
        )


    # ========================================================
    # TEST DISPLAY METHOD
    # ========================================================

    def test_display(self):
        """
        Verify that display() executes without an exception.

        The purpose here is to test that the method works.
        We are not testing console formatting.
        """

        transaction = Transaction(
            transaction_id=7,
            transaction_type="DEPOSIT",
            amount=3000,
            account_number=1006,
            timestamp=datetime.now()
        )

        transaction.display()


# ============================================================
# TEST RUNNER
# ============================================================

if __name__ == "__main__":
    unittest.main()