# ============================================================
# Project 02 : Hospital Management System
# File        : services/appointment_service.py
# Purpose     : Appointment business operations
# ============================================================


from models.appointment import Appointment

from exceptions.hospital_exceptions import (
    PatientNotFoundError,
    DoctorNotFoundError,
    AppointmentNotFoundError
)


class AppointmentService:
    """
    Handles appointment-related business operations.

    Responsibilities:
        - Create appointments
        - Find appointments
        - Cancel appointments
        - Complete appointments
        - View patient appointments
        - View doctor appointments
    """

    def __init__(self):

        # ----------------------------------------------------
        # In-memory appointment storage
        # ----------------------------------------------------

        self.appointments = []

        # ----------------------------------------------------
        # ID generator
        # ----------------------------------------------------

        self.next_appointment_id = 1

    # ========================================================
    # CREATE APPOINTMENT
    # ========================================================

    def create_appointment(
        self,
        patient_service,
        doctor_service,
        patient_id,
        doctor_id,
        date,
        time
    ):
        """
        Create an appointment between a patient and doctor.

        The services are passed into this method so that
        AppointmentService does not need to own patients
        or doctors itself.
        """

        # ----------------------------------------------------
        # Verify patient exists
        # ----------------------------------------------------

        patient = patient_service.find_patient(
            patient_id
        )

        # ----------------------------------------------------
        # Verify doctor exists
        # ----------------------------------------------------

        doctor = doctor_service.find_doctor(
            doctor_id
        )

        # ----------------------------------------------------
        # Create appointment
        # ----------------------------------------------------

        appointment = Appointment(
            appointment_id=self.next_appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            time=time
        )

        # ----------------------------------------------------
        # Store appointment
        # ----------------------------------------------------

        self.appointments.append(appointment)

        # ----------------------------------------------------
        # Connect appointment to patient
        # ----------------------------------------------------

        patient.add_appointment(
            appointment
        )

        # ----------------------------------------------------
        # Connect appointment to doctor
        # ----------------------------------------------------

        doctor.add_appointment(
            appointment
        )

        self.next_appointment_id += 1

        return appointment

    # ========================================================
    # FIND APPOINTMENT
    # ========================================================

    def find_appointment(self, appointment_id):
        """
        Find an appointment by ID.
        """

        for appointment in self.appointments:

            if appointment.appointment_id == appointment_id:

                return appointment

        raise AppointmentNotFoundError(
            appointment_id
        )

    # ========================================================
    # CANCEL APPOINTMENT
    # ========================================================

    def cancel_appointment(self, appointment_id):
        """
        Cancel an existing appointment.
        """

        appointment = self.find_appointment(
            appointment_id
        )

        appointment.cancel()

        return appointment

    # ========================================================
    # COMPLETE APPOINTMENT
    # ========================================================

    def complete_appointment(self, appointment_id):
        """
        Mark an appointment as completed.
        """

        appointment = self.find_appointment(
            appointment_id
        )

        appointment.complete()

        return appointment

    # ========================================================
    # PATIENT APPOINTMENTS
    # ========================================================

    def get_patient_appointments(
        self,
        patient_service,
        patient_id
    ):
        """
        Return all appointments belonging to a patient.
        """

        patient = patient_service.find_patient(
            patient_id
        )

        return patient.appointments

    # ========================================================
    # DOCTOR APPOINTMENTS
    # ========================================================

    def get_doctor_appointments(
        self,
        doctor_service,
        doctor_id
    ):
        """
        Return all appointments belonging to a doctor.
        """

        doctor = doctor_service.find_doctor(
            doctor_id
        )

        return doctor.appointments

    # ========================================================
    # DISPLAY APPOINTMENT
    # ========================================================

    def display_appointment(self, appointment_id):
        """
        Display a single appointment.
        """

        appointment = self.find_appointment(
            appointment_id
        )

        appointment.display()

    # ========================================================
    # DISPLAY ALL APPOINTMENTS
    # ========================================================

    def display_appointments(self):
        """
        Display all appointments.
        """

        if not self.appointments:

            print("\nNo appointments found.")

            return

        print()
        print("=" * 60)
        print("HOSPITAL APPOINTMENTS")
        print("=" * 60)

        for appointment in self.appointments:

            appointment.display()