# ============================================================
# Project 02 : Hospital Management System
# File        : services/doctor_service.py
# Purpose     : Doctor business operations
# ============================================================


from models.doctor import Doctor
from models.department import Department

from exceptions.hospital_exceptions import (
    DoctorNotFoundError,
    DepartmentNotFoundError
)


class DoctorService:
    """
    Handles doctor and department operations.

    Responsibilities:
        - Register doctors
        - Find doctors
        - Create departments
        - Assign doctors to departments
        - Display doctors
        - Display departments
    """

    def __init__(self):

        # ----------------------------------------------------
        # In-memory storage
        # ----------------------------------------------------

        self.doctors = []

        self.departments = []

        # ----------------------------------------------------
        # ID generators
        # ----------------------------------------------------

        self.next_doctor_id = 1

        self.next_department_id = 1

    # ========================================================
    # REGISTER DOCTOR
    # ========================================================

    def register_doctor(
        self,
        name,
        age,
        phone,
        specialization
    ):
        """
        Register a new doctor.
        """

        doctor = Doctor(
            doctor_id=self.next_doctor_id,
            name=name,
            age=age,
            phone=phone,
            specialization=specialization
        )

        self.doctors.append(doctor)

        self.next_doctor_id += 1

        return doctor

    # ========================================================
    # FIND DOCTOR
    # ========================================================

    def find_doctor(self, doctor_id):
        """
        Find a doctor by doctor ID.
        """

        for doctor in self.doctors:

            if doctor.doctor_id == doctor_id:
                return doctor

        raise DoctorNotFoundError(doctor_id)

    # ========================================================
    # CREATE DEPARTMENT
    # ========================================================

    def create_department(self, name):
        """
        Create a new hospital department.
        """

        department = Department(
            department_id=self.next_department_id,
            name=name
        )

        self.departments.append(department)

        self.next_department_id += 1

        return department

    # ========================================================
    # FIND DEPARTMENT
    # ========================================================

    def find_department(self, department_id):
        """
        Find a department by ID.
        """

        for department in self.departments:

            if department.department_id == department_id:
                return department

        raise DepartmentNotFoundError(department_id)

    # ========================================================
    # ASSIGN DOCTOR TO DEPARTMENT
    # ========================================================

    def assign_doctor_to_department(
        self,
        doctor_id,
        department_id
    ):
        """
        Assign an existing doctor to a department.
        """

        doctor = self.find_doctor(doctor_id)

        department = self.find_department(
            department_id
        )

        department.add_doctor(doctor)

        return doctor

    # ========================================================
    # GET DOCTORS BY DEPARTMENT
    # ========================================================

    def get_doctors_by_department(
        self,
        department_id
    ):
        """
        Return doctors belonging to a department.
        """

        department = self.find_department(
            department_id
        )

        return department.get_doctors()

    # ========================================================
    # DISPLAY DOCTOR
    # ========================================================

    def display_doctor(self, doctor_id):
        """
        Display one doctor's information.
        """

        doctor = self.find_doctor(doctor_id)

        doctor.display()

    # ========================================================
    # DISPLAY ALL DOCTORS
    # ========================================================

    def display_doctors(self):
        """
        Display all registered doctors.
        """

        if not self.doctors:

            print("\nNo doctors found.")

            return

        print()
        print("=" * 60)
        print("REGISTERED DOCTORS")
        print("=" * 60)

        for doctor in self.doctors:

            doctor.display()

    # ========================================================
    # DISPLAY DEPARTMENT
    # ========================================================

    def display_department(self, department_id):
        """
        Display one department and its doctors.
        """

        department = self.find_department(
            department_id
        )

        department.display()

        doctors = department.get_doctors()

        if not doctors:

            print("\nNo doctors assigned.")

            return

        print("\nDoctors:")

        for doctor in doctors:

            print(
                f"  {doctor.doctor_id} - "
                f"{doctor.name} - "
                f"{doctor.specialization}"
            )

    # ========================================================
    # DISPLAY ALL DEPARTMENTS
    # ========================================================

    def display_departments(self):
        """
        Display all hospital departments.
        """

        if not self.departments:

            print("\nNo departments found.")

            return

        print()
        print("=" * 60)
        print("HOSPITAL DEPARTMENTS")
        print("=" * 60)

        for department in self.departments:

            department.display()