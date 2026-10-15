# ============================================================
# Project 01 : Bank Management System
# File        : tests/test_customer.py
# Purpose     : Test Customer class
# Testing     : unittest
# ============================================================


# ------------------------------------------------------------
# Import unittest
# ------------------------------------------------------------
# unittest is Python's built-in testing framework.
#
# It provides:
#
#     TestCase
#     assertEqual()
#     assertTrue()
#     assertFalse()
#     assertIs()
#     assertRaises()
#
# We will use these to verify our Customer class.
# ------------------------------------------------------------

import unittest


# ------------------------------------------------------------
# Import Customer
# ------------------------------------------------------------

from models.customer import Customer


# ============================================================
# CUSTOMER TEST CLASS
# ============================================================

class TestCustomer(unittest.TestCase):
    """
    Test cases for the Customer class.
    """


    # ========================================================
    # TEST CUSTOMER CREATION
    # ========================================================

    def test_customer_creation(self):
        """
        Verify that a Customer object is created correctly.
        """

        customer = Customer(
            customer_id=1,
            name="Alex",
            email="alex@example.com"
        )

        # ----------------------------------------------------
        # Verify Customer ID
        # ----------------------------------------------------

        self.assertEqual(
            customer.customer_id,
            1
        )

        # ----------------------------------------------------
        # Verify Customer Name
        # ----------------------------------------------------

        self.assertEqual(
            customer.name,
            "Alex"
        )

        # ----------------------------------------------------
        # Verify Customer Email
        # ----------------------------------------------------

        self.assertEqual(
            customer.email,
            "alex@example.com"
        )


    # ========================================================
    # TEST INITIAL ACCOUNT LIST
    # ========================================================

    def test_customer_starts_without_accounts(self):
        """
        A newly created customer should not have any accounts.
        """

        customer = Customer(
            customer_id=2,
            name="John",
            email="john@example.com"
        )

        self.assertEqual(
            len(customer.accounts),
            0
        )


    # ========================================================
    # TEST ADD ACCOUNT
    # ========================================================

    def test_add_account(self):
        """
        Verify that an account can be added to a customer.
        """

        customer = Customer(
            customer_id=3,
            name="David",
            email="david@example.com"
        )

        # ----------------------------------------------------
        # We don't need a real Account object for this test.
        #
        # A simple object is enough to verify that the
        # Customer.accounts collection works correctly.
        # ----------------------------------------------------

        account = object()

        customer.add_account(account)

        self.assertEqual(
            len(customer.accounts),
            1
        )

        self.assertIn(
            account,
            customer.accounts
        )


    # ========================================================
    # TEST REMOVE ACCOUNT
    # ========================================================

    def test_remove_account(self):
        """
        Verify that an account can be removed.
        """

        customer = Customer(
            customer_id=4,
            name="Sarah",
            email="sarah@example.com"
        )

        account = object()

        customer.add_account(account)

        customer.remove_account(account)

        self.assertEqual(
            len(customer.accounts),
            0
        )

        self.assertNotIn(
            account,
            customer.accounts
        )


    # ========================================================
    # TEST GET ACCOUNTS
    # ========================================================

    def test_get_accounts(self):
        """
        Verify that get_accounts() returns the customer's
        accounts.
        """

        customer = Customer(
            customer_id=5,
            name="Mike",
            email="mike@example.com"
        )

        account1 = object()
        account2 = object()

        customer.add_account(account1)
        customer.add_account(account2)

        accounts = customer.get_accounts()

        self.assertEqual(
            len(accounts),
            2
        )

        self.assertIn(
            account1,
            accounts
        )

        self.assertIn(
            account2,
            accounts
        )


    # ========================================================
    # TEST DISPLAY DETAILS
    # ========================================================

    def test_display_details(self):
        """
        Verify that display_details() executes successfully.

        We are not testing the printed text here.
        We are simply ensuring that the method does not
        raise an exception.
        """

        customer = Customer(
            customer_id=6,
            name="Robert",
            email="robert@example.com"
        )

        customer.display_details()


    # ========================================================
    # TEST __STR__
    # ========================================================

    def test_string_representation(self):
        """
        Verify the Customer.__str__() method.
        """

        customer = Customer(
            customer_id=7,
            name="Alex",
            email="alex@example.com"
        )

        result = str(customer)

        self.assertIn(
            "Alex",
            result
        )

        self.assertIn(
            "alex@example.com",
            result
        )


# ============================================================
# TEST RUNNER
# ============================================================
# When this file is executed directly:
#
#     python -m unittest tests.test_customer
#
# unittest will discover and execute the test methods.
# ============================================================

if __name__ == "__main__":
    unittest.main()