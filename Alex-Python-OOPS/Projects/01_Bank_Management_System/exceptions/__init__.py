# ============================================================
# Project 01 : Bank Management System
# File        : exceptions/__init__.py
# Package     : exceptions
# ============================================================

# This file marks the exceptions directory as a Python package.
#
# The exceptions package contains application-specific
# exceptions used by the banking system.
#
# Instead of using only generic exceptions such as:
#
#     ValueError
#     Exception
#
# we create meaningful banking exceptions such as:
#
#     CustomerNotFoundError
#     AccountNotFoundError
#     InsufficientBalanceError
#     InvalidAmountError
#
# This makes the application easier to understand,
# debug, maintain, and test.