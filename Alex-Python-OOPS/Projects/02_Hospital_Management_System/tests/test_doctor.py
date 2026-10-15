# ============================================================
# Project 02 : Hospital Management System
# File        : tests/test_doctor.py
# Purpose     : Unit tests for Doctor and DoctorService
# ============================================================

import unittest

from models.doctor import Doctor
from models.department import Department

from services.doctor_service import DoctorService

from exceptions.hospital_exceptions import (
    DoctorNotFoundError,
    DepartmentNotFoundError
)


class TestDoctor(unittest.TestCase):

    # ========================================================
    # DOCTOR OBJECT CREATION
    # ========================================================

    def test_doctor_creation(self):

        doctor = Doctor(
            doctor_id=1,
            name="Dr. Ravi",
            age=45,
            phone="9999999999",
            specialization="Cardiology"
        )

        self.assertEqual(
            doctor.doctor_id,
            1
        )

        self.assertEqual(
            doctor.name,
            "Dr. Ravi"
        )

        self.assertEqual(
            doctor.age,
            45
        )

        self.assertEqual(
            doctor.phone,
            "9999999999"
        )

        self.assertEqual(
            doctor.specialization,
            "Cardiology"
        )

    # ========================================================
    # DOCTOR APPOINTMENTS
    # ========================================================

    def test_doctor_appointments(self):

        doctor = Doctor(
            1,
            "Dr. Ravi",
            45,
            "9999999999",
            "Cardiology"
        )

        self.assertEqual(
            len(doctor.appointments),
            0
        )

    # ========================================================
    # DOCTOR STRING
    # ========================================================

    def test_doctor_string(self):

        doctor = Doctor(
            1,
            "Dr. Ravi",
            45,
            "9999999999",
            "Cardiology"
        )

        self.assertEqual(
            str(doctor),
            "Dr. Dr. Ravi - Cardiology"
        )


class TestDoctorService(unittest.TestCase):

    # ========================================================
    # SETUP
    # ========================================================

    def setUp(self):

        self.service = DoctorService()

    # ========================================================
    # REGISTER DOCTOR
    # ========================================================

    def test_register_doctor(self):

        doctor = self.service.register_doctor(
            name="Dr. Ravi",
            age=45,
            phone="9999999999",
            specialization="Cardiology"
        )

        self.assertEqual(
            doctor.doctor_id,
            1
        )

        self.assertEqual(
            doctor.name,
            "Dr. Ravi"
        )

        self.assertEqual(
            doctor.specialization,
            "Cardiology"
        )

        self.assertEqual(
            len(self.service.doctors),
            1
        )

    # ========================================================
    # FIND DOCTOR
    # ========================================================

    def test_find_doctor(self):

        doctor = self.service.register_doctor(
            "Dr. Ravi",
            45,
            "9999999999",
            "Cardiology"
        )

        result = self.service.find_doctor(
            doctor.doctor_id
        )

        self.assertEqual(
            result,
            doctor
        )

    # ========================================================
    # DOCTOR NOT FOUND
    # ========================================================

    def test_doctor_not_found(self):

        with self.assertRaises(
            DoctorNotFoundError
        ):

            self.service.find_doctor(999)

    # ========================================================
    # CREATE DEPARTMENT
    # ========================================================

    def test_create_department(self):

        department = self.service.create_department(
            "Cardiology"
        )

        self.assertEqual(
            department.department_id,
            1
        )

        self.assertEqual(
            department.name,
            "Cardiology"
        )

        self.assertEqual(
            len(self.service.departments),
            1
        )

    # ========================================================
    # FIND DEPARTMENT
    # ========================================================

    def test_find_department(self):

        department = self.service.create_department(
            "Cardiology"
        )

        result = self.service.find_department(
            department.department_id
        )

        self.assertEqual(
            result,
            department
        )

    # ========================================================
    # DEPARTMENT NOT FOUND
    # ========================================================

    def test_department_not_found(self):

        with self.assertRaises(
            DepartmentNotFoundError
        ):

            self.service.find_department(999)

    # ========================================================
    # ASSIGN DOCTOR TO DEPARTMENT
    # ========================================================

    def test_assign_doctor_to_department(self):

        doctor = self.service.register_doctor(
            "Dr. Ravi",
            45,
            "9999999999",
            "Cardiology"
        )

        department = self.service.create_department(
            "Cardiology"
        )

        result = self.service.assign_doctor_to_department(
            doctor.doctor_id,
            department.department_id
        )

        self.assertEqual(
            result,
            doctor
        )

        self.assertEqual(
            len(department.doctors),
            1
        )

        self.assertEqual(
            department.doctors[0],
            doctor
        )

    # ========================================================
    # GET DOCTORS BY DEPARTMENT
    # ========================================================

    def test_get_doctors_by_department(self):

        doctor = self.service.register_doctor(
            "Dr. Ravi",
            45,
            "9999999999",
            "Cardiology"
        )

        department = self.service.create_department(
            "Cardiology"
        )

        self.service.assign_doctor_to_department(
            doctor.doctor_id,
            department.department_id
        )

        doctors = self.service.get_doctors_by_department(
            department.department_id
        )

        self.assertEqual(
            len(doctors),
            1
        )

        self.assertEqual(
            doctors[0],
            doctor
        )


if __name__ == "__main__":

    unittest.main()