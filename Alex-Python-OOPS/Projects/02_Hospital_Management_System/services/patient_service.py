# ============================================================
# Project 02 : Hospital Management System
# File        : services/patient_service.py
# Purpose     : Patient business operations
# ============================================================


from models.patient import Patient
from models.medical_record import MedicalRecord
from models.bill import Bill

from exceptions.hospital_exceptions import (
    PatientNotFoundError,
    InvalidAmountError
)


class PatientService:
    """
    Handles patient-related business operations.

    Responsibilities:
        - Register patients
        - Find patients
        - Add medical records
        - Create bills
        - Display patients
    """

    def __init__(self):

        # ----------------------------------------------------
        # In-memory patient storage
        # ----------------------------------------------------

        self.patients = []

        # ----------------------------------------------------
        # Medical records and bills
        # ----------------------------------------------------

        self.medical_records = []

        self.bills = []

        # ----------------------------------------------------
        # ID generators
        # ----------------------------------------------------

        self.next_patient_id = 1

        self.next_record_id = 1

        self.next_bill_id = 1


    # ========================================================
    # REGISTER PATIENT
    # ========================================================

    def register_patient(
        self,
        name,
        age,
        phone,
        blood_group
    ):
        """
        Register a new patient.
        """

        patient = Patient(
            patient_id=self.next_patient_id,
            name=name,
            age=age,
            phone=phone,
            blood_group=blood_group
        )

        self.patients.append(patient)

        self.next_patient_id += 1

        return patient


    # ========================================================
    # FIND PATIENT
    # ========================================================

    def find_patient(self, patient_id):
        """
        Find a patient using patient ID.

        Raises:
            PatientNotFoundError
        """

        for patient in self.patients:

            if patient.patient_id == patient_id:

                return patient

        raise PatientNotFoundError(patient_id)


    # ========================================================
    # ADD MEDICAL RECORD
    # ========================================================

    def add_medical_record(
        self,
        patient_id,
        doctor_id,
        diagnosis,
        treatment,
        date
    ):
        """
        Add a medical record for a patient.
        """

        patient = self.find_patient(patient_id)

        record = MedicalRecord(
            record_id=self.next_record_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            diagnosis=diagnosis,
            treatment=treatment,
            date=date
        )

        self.medical_records.append(record)

        patient.add_medical_record(record)

        self.next_record_id += 1

        return record


    # ========================================================
    # GET MEDICAL RECORDS
    # ========================================================

    def get_medical_records(self, patient_id):
        """
        Return all medical records of a patient.
        """

        patient = self.find_patient(patient_id)

        return patient.medical_records


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

        patient = self.find_patient(patient_id)

        # ----------------------------------------------------
        # Validate amount
        # ----------------------------------------------------

        if amount <= 0:

            raise InvalidAmountError(amount)

        # ----------------------------------------------------
        # Create bill
        # ----------------------------------------------------

        bill = Bill(
            bill_id=self.next_bill_id,
            patient_id=patient_id,
            amount=amount,
            description=description
        )

        self.bills.append(bill)

        self.next_bill_id += 1

        return bill


    # ========================================================
    # GET PATIENT BILLS
    # ========================================================

    def get_patient_bills(self, patient_id):
        """
        Return all bills belonging to a patient.
        """

        # Make sure patient exists.
        self.find_patient(patient_id)

        result = []

        for bill in self.bills:

            if bill.patient_id == patient_id:

                result.append(bill)

        return result


    # ========================================================
    # DISPLAY PATIENT
    # ========================================================

    def display_patient(self, patient_id):
        """
        Display a patient's details.
        """

        patient = self.find_patient(patient_id)

        patient.display()


    # ========================================================
    # DISPLAY ALL PATIENTS
    # ========================================================

    def display_patients(self):
        """
        Display all registered patients.
        """

        if not self.patients:

            print("\nNo patients found.")

            return

        print()
        print("=" * 60)
        print("REGISTERED PATIENTS")
        print("=" * 60)

        for patient in self.patients:

            patient.display()

    # ========================================================
    # DISPLAY MEDICAL RECORDS
    # ========================================================

    def display_medical_records(self, patient_id):
        """
        Display all medical records for a patient.
        """

        records = self.get_medical_records(
            patient_id
        )

        if not records:

            print("\nNo medical records found.")

            return

        for record in records:

            record.display()


    # ========================================================
    # DISPLAY BILLS
    # ========================================================

    def display_bills(self, patient_id):
        """
        Display all bills for a patient.
        """

        bills = self.get_patient_bills(
            patient_id
        )

        if not bills:

            print("\nNo bills found.")

            return

        for bill in bills:

            bill.display()