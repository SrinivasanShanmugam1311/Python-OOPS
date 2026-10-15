# ============================================================
# Project 01 : Bank Management System
# File        : tests/test_account.py
# Purpose     : Test Account, SavingsAccount and CurrentAccount
# Testing     : unittest
# ============================================================


# ------------------------------------------------------------
# Import unittest
# ------------------------------------------------------------

import unittest


# ------------------------------------------------------------
# Import Account Classes
# ------------------------------------------------------------

from models.account import Account
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount


# ============================================================
# ACCOUNT TESTS
# ============================================================

class TestAccount(unittest.TestCase):
    """
    Test cases for the Account hierarchy.

    Account
       |
       +---- SavingsAccount
       |
       +---- CurrentAccount
    """


    # ========================================================
    # TEST SAVINGS ACCOUNT CREATION
    # ========================================================

    def test_savings_account_creation(self):
        """
        Verify that a SavingsAccount is created correctly.
        """

        account = SavingsAccount(
            account_number=1001,
            holder="Alex",
            balance=5000
        )

        self.assertEqual(
            account.account_number,
            1001
        )

        self.assertEqual(
            account.holder,
            "Alex"
        )

        self.assertEqual(
            account.get_balance(),
            5000
        )


    # ========================================================
    # TEST CURRENT ACCOUNT CREATION
    # ========================================================

    def test_current_account_creation(self):
        """
        Verify that a CurrentAccount is created correctly.
        """

        account = CurrentAccount(
            account_number=1002,
            holder="John",
            balance=3000
        )

        self.assertEqual(
            account.account_number,
            1002
        )

        self.assertEqual(
            account.holder,
            "John"
        )

        self.assertEqual(
            account.get_balance(),
            3000
        )


    # ========================================================
    # TEST DEPOSIT
    # ========================================================

    def test_deposit(self):
        """
        Verify that money can be deposited.
        """

        account = SavingsAccount(
            account_number=1003,
            holder="David",
            balance=1000
        )

        account.deposit(500)

        self.assertEqual(
            account.get_balance(),
            1500
        )


    # ========================================================
    # TEST MULTIPLE DEPOSITS
    # ========================================================

    def test_multiple_deposits(self):
        """
        Verify that multiple deposits update the balance
        correctly.
        """

        account = SavingsAccount(
            account_number=1004,
            holder="Sarah",
            balance=1000
        )

        account.deposit(500)
        account.deposit(250)
        account.deposit(750)

        self.assertEqual(
            account.get_balance(),
            2500
        )


    # ========================================================
    # TEST INVALID DEPOSIT
    # ========================================================

    def test_invalid_deposit(self):
        """
        Deposit amount must be greater than zero.
        """

        account = SavingsAccount(
            account_number=1005,
            holder="Mike",
            balance=1000
        )

        with self.assertRaises(ValueError):

            account.deposit(0)

        with self.assertRaises(ValueError):

            account.deposit(-500)


    # ========================================================
    # TEST SAVINGS WITHDRAWAL
    # ========================================================

    def test_savings_withdrawal(self):
        """
        Verify that a savings account can withdraw money.
        """

        account = SavingsAccount(
            account_number=1006,
            holder="Alex",
            balance=5000
        )

        account.withdraw(2000)

        self.assertEqual(
            account.get_balance(),
            3000
        )


    # ========================================================
    # TEST SAVINGS INSUFFICIENT BALANCE
    # ========================================================

    def test_savings_insufficient_balance(self):
        """
        SavingsAccount should not allow withdrawal greater
        than the available balance.
        """

        account = SavingsAccount(
            account_number=1007,
            holder="Alex",
            balance=1000
        )

        with self.assertRaises(ValueError):

            account.withdraw(1500)


    # ========================================================
    # TEST SAVINGS INVALID WITHDRAWAL
    # ========================================================

    def test_savings_invalid_withdrawal(self):
        """
        Withdrawal amount must be greater than zero.
        """

        account = SavingsAccount(
            account_number=1008,
            holder="Alex",
            balance=1000
        )

        with self.assertRaises(ValueError):

            account.withdraw(0)

        with self.assertRaises(ValueError):

            account.withdraw(-100)


    # ========================================================
    # TEST CURRENT ACCOUNT NORMAL WITHDRAWAL
    # ========================================================

    def test_current_account_withdrawal(self):
        """
        Verify normal withdrawal from CurrentAccount.
        """

        account = CurrentAccount(
            account_number=1009,
            holder="John",
            balance=5000
        )

        account.withdraw(3000)

        self.assertEqual(
            account.get_balance(),
            2000
        )


    # ========================================================
    # TEST CURRENT ACCOUNT OVERDRAFT
    # ========================================================

    def test_current_account_overdraft(self):
        """
        CurrentAccount supports an overdraft facility.

        Example:

            Balance       = 1000
            Overdraft     = 5000
            Maximum       = 6000

        Therefore withdrawal of 4000 is allowed.
        """

        account = CurrentAccount(
            account_number=1010,
            holder="John",
            balance=1000
        )

        account.withdraw(4000)

        self.assertEqual(
            account.get_balance(),
            -3000
        )


    # ========================================================
    # TEST CURRENT ACCOUNT OVERDRAFT LIMIT
    # ========================================================

    def test_current_account_overdraft_limit(self):
        """
        Withdrawal beyond balance + overdraft limit should
        raise an exception.
        """

        account = CurrentAccount(
            account_number=1011,
            holder="John",
            balance=1000
        )

        with self.assertRaises(ValueError):

            account.withdraw(6001)


    # ========================================================
    # TEST ACCOUNT ENCAPSULATION
    # ========================================================

    def test_balance_is_encapsulated(self):
        """
        Verify that balance is stored using a private variable.

        Account uses:

            self.__balance

        Therefore direct access using:

            account.__balance

        should not work.
        """

        account = SavingsAccount(
            account_number=1012,
            holder="Alex",
            balance=5000
        )

        with self.assertRaises(AttributeError):

            print(account.__balance)


    # ========================================================
    # TEST ACCOUNT STRING
    # ========================================================

    def test_account_string(self):
        """
        Verify the __str__() method inherited from Account.
        """

        account = SavingsAccount(
            account_number=1013,
            holder="Alex",
            balance=5000
        )

        result = str(account)

        self.assertIn(
            "1013",
            result
        )

        self.assertIn(
            "Alex",
            result
        )

        self.assertIn(
            "5000",
            result
        )


    # ========================================================
    # TEST POLYMORPHISM
    # ========================================================

    def test_withdraw_polymorphism(self):
        """
        Demonstrate runtime polymorphism.

        Both objects have the same interface:

            withdraw()

        But each account type provides its own implementation.
        """

        accounts = [

            SavingsAccount(
                account_number=1014,
                holder="Alex",
                balance=5000
            ),

            CurrentAccount(
                account_number=1015,
                holder="John",
                balance=5000
            )
        ]


        # ----------------------------------------------------
        # Same method call
        # ----------------------------------------------------
        # Python decides which withdraw() implementation
        # should execute based on the actual object.
        # ----------------------------------------------------

        accounts[0].withdraw(1000)

        accounts[1].withdraw(1000)


        self.assertEqual(
            accounts[0].get_balance(),
            4000
        )

        self.assertEqual(
            accounts[1].get_balance(),
            4000
        )


# ============================================================
# TEST RUNNER
# ============================================================

if __name__ == "__main__":
    unittest.main()