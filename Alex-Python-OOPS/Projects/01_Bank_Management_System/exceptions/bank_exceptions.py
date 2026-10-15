# ============================================================
# Project 01 : Bank Management System
# File        : exceptions/bank_exceptions.py
# Purpose     : Custom exceptions for banking operations
# ============================================================


# ============================================================
# BASE BANK EXCEPTION
# ============================================================

class BankError(Exception):
    """
    Base exception for the Bank Management System.

    All application-specific banking exceptions will inherit
    from this class.

    This allows us to handle all banking errors together:

        except BankError:
            ...

    while still allowing us to handle specific errors when
    required.
    """

    pass


# ============================================================
# CUSTOMER EXCEPTIONS
# ============================================================

class CustomerNotFoundError(BankError):
    """
    Raised when a requested customer does not exist.
    """

    def __init__(self, customer_id):

        self.customer_id = customer_id

        super().__init__(
            f"Customer not found: {customer_id}"
        )


class CustomerAlreadyExistsError(BankError):
    """
    Raised when an attempt is made to create a customer
    that already exists.
    """

    def __init__(self, customer_id):

        self.customer_id = customer_id

        super().__init__(
            f"Customer already exists: {customer_id}"
        )


# ============================================================
# ACCOUNT EXCEPTIONS
# ============================================================

class AccountNotFoundError(BankError):
    """
    Raised when a requested bank account does not exist.
    """

    def __init__(self, account_number):

        self.account_number = account_number

        super().__init__(
            f"Account not found: {account_number}"
        )


class AccountAlreadyExistsError(BankError):
    """
    Raised when an account already exists.
    """

    def __init__(self, account_number):

        self.account_number = account_number

        super().__init__(
            f"Account already exists: {account_number}"
        )


# ============================================================
# MONEY / TRANSACTION EXCEPTIONS
# ============================================================

class InvalidAmountError(BankError):
    """
    Raised when a transaction amount is invalid.

    Examples:

        Negative amount
        Zero amount
        Invalid deposit
        Invalid withdrawal
    """

    def __init__(self, amount):

        self.amount = amount

        super().__init__(
            f"Invalid transaction amount: {amount}"
        )


class InsufficientBalanceError(BankError):
    """
    Raised when an account does not have enough money
    for a withdrawal.
    """

    def __init__(
        self,
        account_number,
        requested_amount,
        available_balance
    ):

        self.account_number = account_number
        self.requested_amount = requested_amount
        self.available_balance = available_balance

        super().__init__(
            f"Insufficient balance in account "
            f"{account_number}. "
            f"Requested: {requested_amount}, "
            f"Available: {available_balance}"
        )


class TransferError(BankError):
    """
    Raised when a money transfer cannot be completed.
    """

    def __init__(self, message):

        super().__init__(message)


# ============================================================
# ACCOUNT OPERATION EXCEPTIONS
# ============================================================

class AccountOperationError(BankError):
    """
    Raised when an account operation cannot be completed.
    """

    def __init__(self, message):

        super().__init__(message)