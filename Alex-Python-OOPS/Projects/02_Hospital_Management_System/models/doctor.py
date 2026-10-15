# ============================================================
# Project 02 : Hospital Management System
# File        : models/doctor.py
# Purpose     : Doctor model
# ============================================================

from models.person import Person


class Doctor(Person):
    """
    Represents a hospital doctor.

    Inherits common properties from Person.
    """

    def __init__(
        self,
        doctor_id,
        name,
        age,
        phone,
        specialization
    ):

        super().__init__(
            person_id=doctor_id,
            name=name,
            age=age,
            phone=phone
        )

        self.doctor_id = doctor_id
        self.specialization = specialization

        # A doctor can have multiple appointments.
        self.appointments = []

    def add_appointment(self, appointment):
        """
        Add an appointment to the doctor's schedule.
        """

        self.appointments.append(appointment)

    def display(self):
        """
        Display doctor information.
        """

        print("=" * 50)
        print("DOCTOR")
        print("=" * 50)

        super().display()

        print("Doctor ID      :", self.doctor_id)
        print("Specialization :", self.specialization)
        print("Appointments   :", len(self.appointments))

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"