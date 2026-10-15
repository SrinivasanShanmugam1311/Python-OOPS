# ============================================================
# Project 02 : Hospital Management System
# File        : tests/test_appointment.py
# Purpose     : Unit tests for Appointment and AppointmentService
# ============================================================

import unittest

from models.appointment import Appointment

from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService

from exceptions.hospital_exceptions import (
    AppointmentNotFoundError
)


class TestAppointment(unittest.TestCase):

    # ========================================================
    # APPOINTMENT CREATION
    # ========================================================

    def test_appointment_creation(self):

        appointment = Appointment(
            appointment_id=1,
            patient_id=10,
            doctor_id=20,
            date="2026-08-10",
            time="10:00 AM"
        )

        self.assertEqual(
            appointment.appointment_id,
            1
        )

        self.assertEqual(
            appointment.patient_id,
            10
        )

        self.assertEqual(
            appointment.doctor_id,
            20
        )

        self.assertEqual(
            appointment.date,
            "2026-08-10"
        )

        self.assertEqual(
            appointment.time,
            "10:00 AM"
        )

        self.assertEqual(
            appointment.status,
            "Scheduled"
        )

    # ========================================================
    # CANCEL APPOINTMENT
    # ========================================================

    def test_cancel_appointment(self):

        appointment = Appointment(
            1,
            10,
            20,
            "2026-08-10",
            "10:00 AM"
        )

        appointment.cancel()

        self.assertEqual(
            appointment.status,
            "Cancelled"
        )

    # ========================================================
    # COMPLETE APPOINTMENT
    # ========================================================

    def test_complete_appointment(self):

        appointment = Appointment(
            1,
            10,
            20,
            "2026-08-10",
            "10:00 AM"
        )

        appointment.complete()

        self.assertEqual(
            appointment.status,
            "Completed"
        )


class TestAppointmentService(unittest.TestCase):

    # ========================================================
    # SETUP
    # ========================================================

    def setUp(self):

        self.patient_service = PatientService()

        self.doctor_service = DoctorService()

        self.appointment_service = (
            AppointmentService()
        )

        # ----------------------------------------------------
        # Create test patient
        # ----------------------------------------------------

        self.patient = (
            self.patient_service.register_patient(
                name="Alex",
                age=45,
                phone="9876543210",
                blood_group="O+"
            )
        )

        # ----------------------------------------------------
        # Create test doctor
        # ----------------------------------------------------

        self.doctor = (
            self.doctor_service.register_doctor(
                name="Dr. Ravi",
                age=45,
                phone="9999999999",
                specialization="Cardiology"
            )
        )

    # ========================================================
    # CREATE APPOINTMENT
    # ========================================================

    def test_create_appointment(self):

        appointment = (
            self.appointment_service.create_appointment(
                patient_service=self.patient_service,
                doctor_service=self.doctor_service,
                patient_id=self.patient.patient_id,
                doctor_id=self.doctor.doctor_id,
                date="2026-08-10",
                time="10:00 AM"
            )
        )

        self.assertEqual(
            appointment.appointment_id,
            1
        )

        self.assertEqual(
            appointment.patient_id,
            self.patient.patient_id
        )

        self.assertEqual(
            appointment.doctor_id,
            self.doctor.doctor_id
        )

        self.assertEqual(
            appointment.status,
            "Scheduled"
        )

    # ========================================================
    # APPOINTMENT STORED IN SERVICE
    # ========================================================

    def test_appointment_stored(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        self.assertEqual(
            len(
                self.appointment_service.appointments
            ),
            1
        )

        self.assertEqual(
            self.appointment_service.appointments[0],
            appointment
        )

    # ========================================================
    # PATIENT APPOINTMENT LINK
    # ========================================================

    def test_patient_appointment_link(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        self.assertEqual(
            len(self.patient.appointments),
            1
        )

        self.assertEqual(
            self.patient.appointments[0],
            appointment
        )

    # ========================================================
    # DOCTOR APPOINTMENT LINK
    # ========================================================

    def test_doctor_appointment_link(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        self.assertEqual(
            len(self.doctor.appointments),
            1
        )

        self.assertEqual(
            self.doctor.appointments[0],
            appointment
        )

    # ========================================================
    # FIND APPOINTMENT
    # ========================================================

    def test_find_appointment(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        result = (
            self.appointment_service.find_appointment(
                appointment.appointment_id
            )
        )

        self.assertEqual(
            result,
            appointment
        )

    # ========================================================
    # APPOINTMENT NOT FOUND
    # ========================================================

    def test_appointment_not_found(self):

        with self.assertRaises(
            AppointmentNotFoundError
        ):

            self.appointment_service.find_appointment(
                999
            )

    # ========================================================
    # CANCEL APPOINTMENT
    # ========================================================

    def test_cancel_appointment(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        result = (
            self.appointment_service.cancel_appointment(
                appointment.appointment_id
            )
        )

        self.assertEqual(
            result.status,
            "Cancelled"
        )

    # ========================================================
    # COMPLETE APPOINTMENT
    # ========================================================

    def test_complete_appointment(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        result = (
            self.appointment_service.complete_appointment(
                appointment.appointment_id
            )
        )

        self.assertEqual(
            result.status,
            "Completed"
        )

    # ========================================================
    # GET PATIENT APPOINTMENTS
    # ========================================================

    def test_get_patient_appointments(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        appointments = (
            self.appointment_service
            .get_patient_appointments(
                self.patient_service,
                self.patient.patient_id
            )
        )

        self.assertEqual(
            len(appointments),
            1
        )

        self.assertEqual(
            appointments[0],
            appointment
        )

    # ========================================================
    # GET DOCTOR APPOINTMENTS
    # ========================================================

    def test_get_doctor_appointments(self):

        appointment = (
            self.appointment_service.create_appointment(
                self.patient_service,
                self.doctor_service,
                self.patient.patient_id,
                self.doctor.doctor_id,
                "2026-08-10",
                "10:00 AM"
            )
        )

        appointments = (
            self.appointment_service
            .get_doctor_appointments(
                self.doctor_service,
                self.doctor.doctor_id
            )
        )

        self.assertEqual(
            len(appointments),
            1
        )

        self.assertEqual(
            appointments[0],
            appointment
        )


if __name__ == "__main__":

    unittest.main()