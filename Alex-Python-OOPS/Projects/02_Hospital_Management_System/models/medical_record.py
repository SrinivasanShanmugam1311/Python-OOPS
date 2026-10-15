# ============================================================
# Project 02 : Hospital Management System
# File        : models/medical_record.py
# Purpose     : Medical record model
# ============================================================

from dataclasses import dataclass


@dataclass
class MedicalRecord:
    """
    Represents a patient's medical record.
    """

    record_id: int
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str
    date: str

    def display(self):
        """
        Display medical record.
        """

        print("=" * 50)
        print("MEDICAL RECORD")
        print("=" * 50)

        print("Record ID  :", self.record_id)
        print("Patient ID :", self.patient_id)
        print("Doctor ID  :", self.doctor_id)
        print("Diagnosis  :", self.diagnosis)
        print("Treatment  :", self.treatment)
        print("Date       :", self.date)