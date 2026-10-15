# ============================================================
# Project 02 : Hospital Management System
# File        : main.py
# Purpose     : Main menu and application entry point
# ============================================================


from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService
from services.billing_service import BillingService

from exceptions.hospital_exceptions import HospitalError


# ============================================================
# SERVICE INITIALIZATION
# ============================================================

patient_service = PatientService()

doctor_service = DoctorService()

appointment_service = AppointmentService(
    )

billing_service = BillingService(
    patient_service
)


# ============================================================
# INPUT HELPERS
# ============================================================

def get_int(prompt):
    """
    Read an integer safely from the user.
    """

    while True:

        try:

            return int(input(prompt))

        except ValueError:

            print("Please enter a valid number.")


def get_float(prompt):
    """
    Read a floating-point number safely.
    """

    while True:

        try:

            return float(input(prompt))

        except ValueError:

            print("Please enter a valid amount.")


# ============================================================
# PATIENT MENU OPERATIONS
# ============================================================

def create_patient():
    """
    Register a new patient.
    """

    print("\n" + "=" * 60)
    print("REGISTER PATIENT")
    print("=" * 60)

    name = input("Name        : ")
    age = get_int("Age         : ")
    phone = input("Phone       : ")
    blood_group = input("Blood Group : ")

    patient = patient_service.register_patient(
        name=name,
        age=age,
        phone=phone,
        blood_group=blood_group
    )

    print("\nPatient registered successfully.")
    print("Patient ID :", patient.patient_id)


def show_patients():
    """
    Display all patients.
    """

    patient_service.display_patients()


def show_patient():
    """
    Display one patient's information.
    """

    patient_id = get_int("Enter Patient ID: ")

    patient_service.display_patient(
        patient_id
    )


# ============================================================
# DOCTOR MENU OPERATIONS
# ============================================================

def create_doctor():
    """
    Register a new doctor.
    """

    print("\n" + "=" * 60)
    print("REGISTER DOCTOR")
    print("=" * 60)

    name = input("Name           : ")
    age = get_int("Age            : ")
    phone = input("Phone          : ")
    specialization = input("Specialization : ")

    doctor = doctor_service.register_doctor(
        name=name,
        age=age,
        phone=phone,
        specialization=specialization
    )

    print("\nDoctor registered successfully.")
    print("Doctor ID :", doctor.doctor_id)


def show_doctors():
    """
    Display all doctors.
    """

    doctor_service.display_doctors()


def create_department():
    """
    Create a hospital department.
    """

    print("\n" + "=" * 60)
    print("CREATE DEPARTMENT")
    print("=" * 60)

    name = input("Department Name: ")

    department = doctor_service.create_department(
        name
    )

    print("\nDepartment created successfully.")
    print("Department ID :", department.department_id)


def assign_doctor():
    """
    Assign a doctor to a department.
    """

    print("\n" + "=" * 60)
    print("ASSIGN DOCTOR TO DEPARTMENT")
    print("=" * 60)

    doctor_id = get_int("Doctor ID     : ")
    department_id = get_int("Department ID : ")

    doctor_service.assign_doctor_to_department(
        doctor_id,
        department_id
    )

    print("\nDoctor assigned successfully.")


def show_departments():
    """
    Display all departments.
    """

    doctor_service.display_departments()


# ============================================================
# APPOINTMENT OPERATIONS
# ============================================================

def create_appointment():
    """
    Create an appointment between a patient and doctor.
    """

    print("\n" + "=" * 60)
    print("CREATE APPOINTMENT")
    print("=" * 60)

    patient_id = get_int("Patient ID : ")
    doctor_id = get_int("Doctor ID  : ")
    date = input("Date        : ")
    time = input("Time        : ")

    appointment = appointment_service.create_appointment(
        patient_service=patient_service,
        doctor_service=doctor_service,
        patient_id=patient_id,
        doctor_id=doctor_id,
        date=date,
        time=time
    )

    print("\nAppointment created successfully.")
    print(
        "Appointment ID :",
        appointment.appointment_id
    )


def show_appointments():
    """
    Display all appointments.
    """

    appointment_service.display_appointments()


def cancel_appointment():
    """
    Cancel an appointment.
    """

    appointment_id = get_int(
        "Appointment ID: "
    )

    appointment_service.cancel_appointment(
        appointment_id
    )

    print("\nAppointment cancelled.")


def complete_appointment():
    """
    Mark an appointment as completed.
    """

    appointment_id = get_int(
        "Appointment ID: "
    )

    appointment_service.complete_appointment(
        appointment_id
    )

    print("\nAppointment completed.")


# ============================================================
# MEDICAL RECORD OPERATIONS
# ============================================================

def add_medical_record():
    """
    Add a medical record for a patient.
    """

    print("\n" + "=" * 60)
    print("ADD MEDICAL RECORD")
    print("=" * 60)

    patient_id = get_int("Patient ID : ")
    doctor_id = get_int("Doctor ID  : ")
    diagnosis = input("Diagnosis   : ")
    treatment = input("Treatment   : ")
    date = input("Date        : ")

    record = patient_service.add_medical_record(
        patient_id=patient_id,
        doctor_id=doctor_id,
        diagnosis=diagnosis,
        treatment=treatment,
        date=date
    )

    print("\nMedical record added successfully.")
    print("Record ID :", record.record_id)


def show_medical_records():
    """
    Display medical records of a patient.
    """

    patient_id = get_int(
        "Patient ID: "
    )

    patient_service.display_medical_records(
        patient_id
    )


# ============================================================
# BILLING OPERATIONS
# ============================================================

def create_bill():
    """
    Create a hospital bill.
    """

    print("\n" + "=" * 60)
    print("CREATE BILL")
    print("=" * 60)

    patient_id = get_int("Patient ID : ")
    amount = get_float("Amount     : ")
    description = input("Description: ")

    bill = billing_service.create_bill(
        patient_id=patient_id,
        amount=amount,
        description=description
    )

    print("\nBill created successfully.")
    print("Bill ID :", bill.bill_id)


def pay_bill():
    """
    Pay an existing bill.
    """

    bill_id = get_int(
        "Bill ID: "
    )

    billing_service.pay_bill(
        bill_id
    )

    print("\nBill paid successfully.")


def show_patient_bills():
    """
    Display all bills for a patient.
    """

    patient_id = get_int(
        "Patient ID: "
    )

    billing_service.display_patient_bills(
        patient_id
    )


def show_all_bills():
    """
    Display all hospital bills.
    """

    billing_service.display_all_bills()


# ============================================================
# MAIN MENU
# ============================================================

def display_menu():
    """
    Display the main application menu.
    """

    print("\n")
    print("=" * 60)
    print("          HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1.  Register Patient")
    print("2.  View Patients")
    print("3.  View Patient")

    print("4.  Register Doctor")
    print("5.  View Doctors")

    print("6.  Create Department")
    print("7.  Assign Doctor to Department")
    print("8.  View Departments")

    print("9.  Create Appointment")
    print("10. View Appointments")
    print("11. Cancel Appointment")
    print("12. Complete Appointment")

    print("13. Add Medical Record")
    print("14. View Medical Records")

    print("15. Create Bill")
    print("16. Pay Bill")
    print("17. View Patient Bills")
    print("18. View All Bills")

    print("0.  Exit")

    print("=" * 60)


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():
    """
    Application entry point.
    """

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        try:

            if choice == "1":

                create_patient()

            elif choice == "2":

                show_patients()

            elif choice == "3":

                show_patient()

            elif choice == "4":

                create_doctor()

            elif choice == "5":

                show_doctors()

            elif choice == "6":

                create_department()

            elif choice == "7":

                assign_doctor()

            elif choice == "8":

                show_departments()

            elif choice == "9":

                create_appointment()

            elif choice == "10":

                show_appointments()

            elif choice == "11":

                cancel_appointment()

            elif choice == "12":

                complete_appointment()

            elif choice == "13":

                add_medical_record()

            elif choice == "14":

                show_medical_records()

            elif choice == "15":

                create_bill()

            elif choice == "16":

                pay_bill()

            elif choice == "17":

                show_patient_bills()

            elif choice == "18":

                show_all_bills()

            elif choice == "0":

                print(
                    "\nThank you for using "
                    "Hospital Management System."
                )

                break

            else:

                print(
                    "\nInvalid choice. "
                    "Please select from the menu."
                )

        except HospitalError as error:

            print(
                "\nHospital Error:",
                error
            )

        except Exception as error:

            print(
                "\nUnexpected Error:",
                error
            )


# ============================================================
# PROGRAM ENTRY
# ============================================================

if __name__ == "__main__":

    main()