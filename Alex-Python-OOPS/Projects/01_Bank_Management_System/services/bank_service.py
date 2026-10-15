# ============================================================
# Project 01 : Bank Management System
# File        : services/bank_service.py
# Purpose     : Banking business logic
# ============================================================


# ============================================================
# IMPORT MODELS
# ============================================================

from models.customer import Customer
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction


# ============================================================
# IMPORT CUSTOM EXCEPTIONS
# ============================================================

from exceptions.bank_exceptions import (
    CustomerNotFoundError,
    AccountNotFoundError,
    InvalidAmountError,
    InsufficientBalanceError
)


# ============================================================
# IMPORT DATETIME
# ============================================================

from datetime import datetime


# ============================================================
# BANK SERVICE
# ============================================================

class BankService:
    """
    Contains the business logic of the banking application.

    main.py
        ↓
    BankService
        ↓
    Models
    """

    def __init__(self):

        # ----------------------------------------------------
        # In-memory storage
        # ----------------------------------------------------

        self.customers = []

        self.accounts = []

        self.transactions = []


        # ----------------------------------------------------
        # ID generators
        # ----------------------------------------------------

        self.next_customer_id = 1

        self.next_account_number = 1001

        self.next_transaction_id = 1


    # ========================================================
    # CUSTOMER OPERATIONS
    # ========================================================

    def create_customer(self, name, email):
        """
        Create and store a customer.
        """

        customer = Customer(
            customer_id=self.next_customer_id,
            name=name,
            email=email
        )

        self.customers.append(customer)

        self.next_customer_id += 1

        return customer


    def find_customer(self, customer_id):
        """
        Find a customer by ID.

        Returns:
            Customer object

        Raises:
            CustomerNotFoundError
        """

        for customer in self.customers:

            if customer.customer_id == customer_id:
                return customer

        raise CustomerNotFoundError(customer_id)


    # ========================================================
    # ACCOUNT SEARCH
    # ========================================================

    def find_account(self, account_number):
        """
        Find an account by account number.

        Raises:
            AccountNotFoundError
        """

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        raise AccountNotFoundError(account_number)


    # ========================================================
    # VALIDATE AMOUNT
    # ========================================================

    def _validate_amount(self, amount):
        """
        Validate a transaction amount.

        Amount must be greater than zero.
        """

        if amount <= 0:

            raise InvalidAmountError(amount)


    # ========================================================
    # CREATE SAVINGS ACCOUNT
    # ========================================================

    def create_savings_account(
        self,
        customer_id,
        initial_balance=0
    ):
        """
        Create a SavingsAccount for a customer.
        """

        # ----------------------------------------------------
        # Validate customer
        # ----------------------------------------------------

        customer = self.find_customer(customer_id)


        # ----------------------------------------------------
        # Validate initial balance
        # ----------------------------------------------------

        if initial_balance < 0:

            raise InvalidAmountError(
                initial_balance
            )


        # ----------------------------------------------------
        # Create account
        # ----------------------------------------------------

        account = SavingsAccount(
            account_number=self.next_account_number,
            holder=customer.name,
            balance=initial_balance
        )


        # ----------------------------------------------------
        # Store account
        # ----------------------------------------------------

        self.accounts.append(account)


        # ----------------------------------------------------
        # Connect account to customer
        # ----------------------------------------------------

        customer.add_account(account)


        self.next_account_number += 1

        return account


    # ========================================================
    # CREATE CURRENT ACCOUNT
    # ========================================================

    def create_current_account(
        self,
        customer_id,
        initial_balance=0
    ):
        """
        Create a CurrentAccount for a customer.
        """

        customer = self.find_customer(customer_id)


        if initial_balance < 0:

            raise InvalidAmountError(
                initial_balance
            )


        account = CurrentAccount(
            account_number=self.next_account_number,
            holder=customer.name,
            balance=initial_balance
        )


        self.accounts.append(account)

        customer.add_account(account)

        self.next_account_number += 1

        return account


    # ========================================================
    # DEPOSIT
    # ========================================================

    def deposit(self, account_number, amount):
        """
        Deposit money into an account.
        """

        # ----------------------------------------------------
        # Validate amount
        # ----------------------------------------------------

        self._validate_amount(amount)


        # ----------------------------------------------------
        # Find account
        # ----------------------------------------------------

        account = self.find_account(account_number)


        # ----------------------------------------------------
        # Deposit
        # ----------------------------------------------------

        account.deposit(amount)


        # ----------------------------------------------------
        # Record transaction
        # ----------------------------------------------------

        transaction = Transaction(
            transaction_id=self.next_transaction_id,
            transaction_type="DEPOSIT",
            amount=amount,
            account_number=account_number,
            timestamp=datetime.now()
        )

        self.transactions.append(transaction)

        self.next_transaction_id += 1


    # ========================================================
    # WITHDRAW
    # ========================================================

    def withdraw(self, account_number, amount):
        """
        Withdraw money from an account.

        The actual withdrawal rule is delegated to the
        account object.

        This demonstrates polymorphism.
        """

        self._validate_amount(amount)

        account = self.find_account(account_number)


        # ----------------------------------------------------
        # Account-specific withdrawal
        # ----------------------------------------------------
        #
        # SavingsAccount:
        #     Checks available balance.
        #
        # CurrentAccount:
        #     Checks balance + overdraft.
        #
        # Same method:
        #
        #     withdraw()
        #
        # Different behavior.
        # ----------------------------------------------------

        try:

            account.withdraw(amount)

        except ValueError:

            # ------------------------------------------------
            # Convert generic model error into a meaningful
            # application-specific exception.
            # ------------------------------------------------

            raise InsufficientBalanceError(
                account_number=account_number,
                requested_amount=amount,
                available_balance=account.get_balance()
            )


        # ----------------------------------------------------
        # Record transaction
        # ----------------------------------------------------

        transaction = Transaction(
            transaction_id=self.next_transaction_id,
            transaction_type="WITHDRAW",
            amount=amount,
            account_number=account_number,
            timestamp=datetime.now()
        )

        self.transactions.append(transaction)

        self.next_transaction_id += 1


    # ========================================================
    # GET BALANCE
    # ========================================================

    def get_balance(self, account_number):
        """
        Return the current balance.
        """

        account = self.find_account(
            account_number
        )

        return account.get_balance()


    # ========================================================
    # TRANSACTION HISTORY
    # ========================================================

    def get_transactions(self, account_number):
        """
        Return transactions for an account.
        """

        # ----------------------------------------------------
        # Make sure account exists.
        # ----------------------------------------------------

        self.find_account(account_number)


        result = []

        for transaction in self.transactions:

            if transaction.account_number == account_number:

                result.append(transaction)

        return result


    def display_transactions(self, account_number):
        """
        Display transaction history.
        """

        transactions = self.get_transactions(
            account_number
        )


        if not transactions:

            print()
            print("No transactions found.")

            return


        print()
        print("=" * 60)
        print("TRANSACTION HISTORY")
        print("=" * 60)


        for transaction in transactions:

            transaction.display()


    # ========================================================
    # DISPLAY CUSTOMERS
    # ========================================================

    def display_customers(self):
        """
        Display all customers.
        """

        if not self.customers:

            print()
            print("No customers found.")

            return


        print()
        print("=" * 60)
        print("CUSTOMERS")
        print("=" * 60)


        for customer in self.customers:

            customer.display_details()


    # ========================================================
    # DISPLAY ACCOUNTS
    # ========================================================

    def display_accounts(self):
        """
        Display all accounts.
        """

        if not self.accounts:

            print()
            print("No accounts found.")

            return


        print()
        print("=" * 60)
        print("BANK ACCOUNTS")
        print("=" * 60)


        for account in self.accounts:

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

            print("-" * 60)