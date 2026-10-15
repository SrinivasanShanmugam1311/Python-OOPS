# ============================================================
# Project 02 : Hospital Management System
# File        : services/billing_service.py
# Purpose     : Hospital billing business operations
# ============================================================


from exceptions.hospital_exceptions import (
    PatientNotFoundError,
    BillNotFoundError,
    InvalidAmountError
)


class BillingService:
    """
    Handles hospital billing operations.

    Responsibilities:
        - Create bills
        - Find bills
        - Pay bills
        - Get patient bills
        - Calculate total bills
        - Display bills
    """

    def __init__(self, patient_service):

        # ----------------------------------------------------
        # Patient service
        # ----------------------------------------------------

        self.patient_service = patient_service

        # ----------------------------------------------------
        # Store all bills
        # ----------------------------------------------------

        self.bills = []

        # ----------------------------------------------------
        # Bill ID generator
        # ----------------------------------------------------

        self.next_bill_id = 1

    # ========================================================
    # CREATE BILL
    # ========================================================

    def create_bill(
        self,
        patient_id,
        amount,
        description
    ):
        """
        Create a bill for a patient.
        """

        # ----------------------------------------------------
        # Verify patient exists
        # ----------------------------------------------------

        patient = self.patient_service.find_patient(
            patient_id
        )

        # ----------------------------------------------------
        # Validate amount
        # ----------------------------------------------------

        if amount <= 0:

            raise InvalidAmountError(amount)

        # ----------------------------------------------------
        # Import Bill model
        # ----------------------------------------------------

        from models.bill import Bill

        # ----------------------------------------------------
        # Create bill
        # ----------------------------------------------------

        bill = Bill(
            bill_id=self.next_bill_id,
            patient_id=patient_id,
            amount=amount,
            description=description
        )

        # ----------------------------------------------------
        # Store bill
        # ----------------------------------------------------

        self.bills.append(bill)

        # ----------------------------------------------------
        # Connect bill to patient
        # ----------------------------------------------------

        if not hasattr(patient, "bills"):

            patient.bills = []

        patient.bills.append(bill)

        self.next_bill_id += 1

        return bill

    # ========================================================
    # FIND BILL
    # ========================================================

    def find_bill(self, bill_id):
        """
        Find a bill by ID.
        """

        for bill in self.bills:

            if bill.bill_id == bill_id:

                return bill

        raise BillNotFoundError(bill_id)

    # ========================================================
    # PAY BILL
    # ========================================================

    def pay_bill(self, bill_id):
        """
        Mark a bill as paid.
        """

        bill = self.find_bill(bill_id)

        bill.pay()

        return bill

    # ========================================================
    # GET PATIENT BILLS
    # ========================================================

    def get_patient_bills(self, patient_id):
        """
        Return all bills belonging to a patient.
        """

        patient = self.patient_service.find_patient(
            patient_id
        )

        if hasattr(patient, "bills"):

            return patient.bills

        return []

    # ========================================================
    # CALCULATE TOTAL
    # ========================================================

    def calculate_total(self, patient_id):
        """
        Calculate the total amount of all bills
        belonging to a patient.
        """

        bills = self.get_patient_bills(
            patient_id
        )

        total = 0

        for bill in bills:

            total += bill.amount

        return total

    # ========================================================
    # CALCULATE PENDING TOTAL
    # ========================================================

    def calculate_pending_total(self, patient_id):
        """
        Calculate the total amount of unpaid bills.
        """

        bills = self.get_patient_bills(
            patient_id
        )

        total = 0

        for bill in bills:

            if bill.status == "Pending":

                total += bill.amount

        return total

    # ========================================================
    # DISPLAY BILL
    # ========================================================

    def display_bill(self, bill_id):
        """
        Display one bill.
        """

        bill = self.find_bill(
            bill_id
        )

        bill.display()

    # ========================================================
    # DISPLAY PATIENT BILLS
    # ========================================================

    def display_patient_bills(self, patient_id):
        """
        Display all bills for a patient.
        """

        bills = self.get_patient_bills(
            patient_id
        )

        if not bills:

            print("\nNo bills found.")

            return

        print()
        print("=" * 60)
        print("PATIENT BILLS")
        print("=" * 60)

        for bill in bills:

            bill.display()

        print()
        print("Total Amount   :", self.calculate_total(patient_id))
        print(
            "Pending Amount :",
            self.calculate_pending_total(patient_id)
        )

    # ========================================================
    # DISPLAY ALL BILLS
    # ========================================================

    def display_all_bills(self):
        """
        Display every hospital bill.
        """

        if not self.bills:

            print("\nNo bills found.")

            return

        print()
        print("=" * 60)
        print("ALL HOSPITAL BILLS")
        print("=" * 60)

        for bill in self.bills:

            bill.display()