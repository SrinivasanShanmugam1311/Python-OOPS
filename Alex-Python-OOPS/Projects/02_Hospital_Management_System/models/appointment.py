# ============================================================
# Project 02 : Hospital Management System
# File        : models/appointment.py
# Purpose     : Appointment model
# ============================================================

from dataclasses import dataclass


@dataclass
class Appointment:
    """
    Represents an appointment between
    a patient and a doctor.
    """

    appointment_id: int
    patient_id: int
    doctor_id: int
    date: str
    time: str
    status: str = "Scheduled"

    def cancel(self):
        """
        Cancel the appointment.
        """

        self.status = "Cancelled"

    def complete(self):
        """
        Mark appointment as completed.
        """

        self.status = "Completed"

    def display(self):
        """
        Display appointment information.
        """

        print("=" * 50)
        print("APPOINTMENT")
        print("=" * 50)

        print("Appointment ID :", self.appointment_id)
        print("Patient ID     :", self.patient_id)
        print("Doctor ID      :", self.doctor_id)
        print("Date           :", self.date)
        print("Time           :", self.time)
        print("Status         :", self.status)