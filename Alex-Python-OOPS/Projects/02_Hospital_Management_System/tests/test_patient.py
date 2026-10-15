# ============================================================
# Project 02 : Hospital Management System
# File        : tests/test_patient.py
# Purpose     : Unit tests for Patient and PatientService
# ============================================================

import unittest

from models.patient import Patient
from services.patient_service import PatientService
from exceptions.hospital_exceptions import PatientNotFoundError


class TestPatient(unittest.TestCase):

    # ========================================================
    # PATIENT OBJECT CREATION
    # ========================================================

    def test_patient_creation(self):

        patient = Patient(
            patient_id=1,
            name="Alex",
            age=45,
            phone="9876543210",
            blood_group="O+"
        )

        self.assertEqual(patient.patient_id, 1)
        self.assertEqual(patient.name, "Alex")
        self.assertEqual(patient.age, 45)
        self.assertEqual(patient.phone, "9876543210")
        self.assertEqual(patient.blood_group, "O+")

    # ========================================================
    # PATIENT COLLECTIONS
    # ========================================================

    def test_patient_collections(self):

        patient = Patient(
            1,
            "Alex",
            45,
            "9876543210",
            "O+"
        )

        self.assertEqual(
            len(patient.appointments),
            0
        )

        self.assertEqual(
            len(patient.medical_records),
            0
        )

    # ========================================================
    # PATIENT STRING
    # ========================================================

    def test_patient_string(self):

        patient = Patient(
            1,
            "Alex",
            45,
            "9876543210",
            "O+"
        )

        self.assertEqual(
            str(patient),
            "Patient(1, Alex)"
        )


class TestPatientService(unittest.TestCase):

    # ========================================================
    # SETUP
    # ========================================================

    def setUp(self):

        self.service = PatientService()

    # ========================================================
    # REGISTER PATIENT
    # ========================================================

    def test_register_patient(self):

        patient = self.service.register_patient(
            name="Alex",
            age=45,
            phone="9876543210",
            blood_group="O+"
        )

        self.assertEqual(
            patient.patient_id,
            1
        )

        self.assertEqual(
            patient.name,
            "Alex"
        )

        self.assertEqual(
            len(self.service.patients),
            1
        )

    # ========================================================
    # FIND PATIENT
    # ========================================================

    def test_find_patient(self):

        patient = self.service.register_patient(
            "Alex",
            45,
            "9876543210",
            "O+"
        )

        result = self.service.find_patient(
            patient.patient_id
        )

        self.assertEqual(
            result,
            patient
        )

    # ========================================================
    # PATIENT NOT FOUND
    # ========================================================

    def test_patient_not_found(self):

        with self.assertRaises(
            PatientNotFoundError
        ):

            self.service.find_patient(999)


if __name__ == "__main__":

    unittest.main()