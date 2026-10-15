# ============================================================
# Project 02 : Hospital Management System
# File        : exceptions/hospital_exceptions.py
# Purpose     : Custom exception hierarchy
# ============================================================


# ============================================================
# BASE EXCEPTION
# ============================================================

class HospitalError(Exception):
    """
    Base exception for the Hospital Management System.

    All application-specific exceptions inherit from this
    class.
    """

    pass


# ============================================================
# PATIENT EXCEPTIONS
# ============================================================

class PatientNotFoundError(HospitalError):
    """
    Raised when a patient cannot be found.
    """

    def __init__(self, patient_id):

        self.patient_id = patient_id

        super().__init__(
            f"Patient not found: {patient_id}"
        )


# ============================================================
# DOCTOR EXCEPTIONS
# ============================================================

class DoctorNotFoundError(HospitalError):
    """
    Raised when a doctor cannot be found.
    """

    def __init__(self, doctor_id):

        self.doctor_id = doctor_id

        super().__init__(
            f"Doctor not found: {doctor_id}"
        )


# ============================================================
# DEPARTMENT EXCEPTIONS
# ============================================================

class DepartmentNotFoundError(HospitalError):
    """
    Raised when a department cannot be found.
    """

    def __init__(self, department_id):

        self.department_id = department_id

        super().__init__(
            f"Department not found: {department_id}"
        )


# ============================================================
# APPOINTMENT EXCEPTIONS
# ============================================================

class AppointmentNotFoundError(HospitalError):
    """
    Raised when an appointment cannot be found.
    """

    def __init__(self, appointment_id):

        self.appointment_id = appointment_id

        super().__init__(
            f"Appointment not found: {appointment_id}"
        )


# ============================================================
# BILLING EXCEPTIONS
# ============================================================

class BillNotFoundError(HospitalError):
    """
    Raised when a bill cannot be found.
    """

    def __init__(self, bill_id):

        self.bill_id = bill_id

        super().__init__(
            f"Bill not found: {bill_id}"
        )


# ============================================================
# VALIDATION EXCEPTION
# ============================================================

class InvalidAmountError(HospitalError):
    """
    Raised when an invalid monetary amount is provided.
    """

    def __init__(self, amount):

        self.amount = amount

        super().__init__(
            f"Invalid amount: {amount}. "
            f"Amount must be greater than zero."
        )


# ============================================================
# OPERATION EXCEPTION
# ============================================================

class InvalidAppointmentError(HospitalError):
    """
    Raised when an appointment operation is invalid.
    """

    def __init__(self, message):

        super().__init__(message)