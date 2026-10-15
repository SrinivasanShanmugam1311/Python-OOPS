# ============================================================
# Project 02 : Hospital Management System
# File        : models/patient.py
# Purpose     : Patient model
# ============================================================

from models.person import Person


class Patient(Person):
    """
    Represents a hospital patient.

    Inherits common properties from Person.
    """

    def __init__(
        self,
        patient_id,
        name,
        age,
        phone,
        blood_group
    ):

        super().__init__(
            person_id=patient_id,
            name=name,
            age=age,
            phone=phone
        )

        self.patient_id = patient_id
        self.blood_group = blood_group

        # A patient can have multiple medical records.
        self.medical_records = []

        # A patient can have multiple appointments.
        self.appointments = []

    def add_medical_record(self, record):
        """
        Add a medical record to the patient.
        """

        self.medical_records.append(record)

    def add_appointment(self, appointment):
        """
        Add an appointment to the patient.
        """

        self.appointments.append(appointment)

    def display(self):
        """
        Display patient information.
        """

        print("=" * 50)
        print("PATIENT")
        print("=" * 50)

        super().display()

        print("Patient ID   :", self.patient_id)
        print("Blood Group  :", self.blood_group)
        print("Appointments :", len(self.appointments))
        print("Records      :", len(self.medical_records))

    def __str__(self):
        return f"Patient({self.patient_id}, {self.name})"