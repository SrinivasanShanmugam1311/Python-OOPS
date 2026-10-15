# ============================================================
# Project 02 : Hospital Management System
# File        : models/department.py
# Purpose     : Hospital department model
# ============================================================


class Department:
    """
    Represents a hospital department.

    Example:
        Cardiology
        Neurology
        Orthopedics
    """

    def __init__(self, department_id, name):

        self.department_id = department_id
        self.name = name

        # Doctors belonging to this department.
        self.doctors = []

    def add_doctor(self, doctor):
        """
        Add a doctor to the department.
        """

        self.doctors.append(doctor)

    def get_doctors(self):
        """
        Return all doctors in the department.
        """

        return self.doctors

    def display(self):
        """
        Display department information.
        """

        print("=" * 50)
        print("DEPARTMENT")
        print("=" * 50)

        print("Department ID :", self.department_id)
        print("Name          :", self.name)
        print("Doctors       :", len(self.doctors))

    def __str__(self):
        return f"{self.department_id} - {self.name}"