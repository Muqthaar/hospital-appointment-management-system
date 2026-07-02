"""
=========================================================
Hospital Appointment Booking System
Reports Module
=========================================================
"""

from data import patients, doctors, appointments
from utils import print_title, line


# ==========================================================
# Overall Summary Report
# ==========================================================

def overall_report():

    pending = 0
    accepted = 0
    rejected = 0
    cancelled = 0

    for appointment in appointments:

        if appointment["status"] == "Pending":
            pending += 1

        elif appointment["status"] == "Accepted":
            accepted += 1

        elif appointment["status"] == "Rejected":
            rejected += 1

        elif appointment["status"] == "Cancelled":
            cancelled += 1

    print_title("HOSPITAL SUMMARY REPORT")

    print(f"Total Patients      : {len(patients)}")
    print(f"Total Doctors       : {len(doctors)}")
    print(f"Total Appointments  : {len(appointments)}")
    print(f"Pending             : {pending}")
    print(f"Accepted            : {accepted}")
    print(f"Rejected            : {rejected}")
    print(f"Cancelled           : {cancelled}")

    line()


# ==========================================================
# Doctor-wise Appointment Count
# ==========================================================

def doctor_wise_report():

    print_title("DOCTOR APPOINTMENT REPORT")

    for doctor in doctors:

        count = 0

        for appointment in appointments:

            if appointment["doctor_id"] == doctor["id"]:
                count += 1

        print(f"{doctor['name']}")
        print(f"Appointments : {count}")

        line()


# ==========================================================
# Disease-wise Patient Report
# ==========================================================

def disease_report():

    print_title("DISEASE REPORT")

    diseases = {}

    for patient in patients:

        disease = patient["disease"]

        if disease in diseases:

            diseases[disease] += 1

        else:

            diseases[disease] = 1

    if not diseases:

        print("No patient records available.")
        return

    for disease, count in diseases.items():

        print(f"{disease:<25} : {count}")

    line()


# ==========================================================
# Appointment Status Report
# ==========================================================

def appointment_status_report():

    pending = 0
    accepted = 0
    rejected = 0
    cancelled = 0

    for appointment in appointments:

        status = appointment["status"]

        if status == "Pending":
            pending += 1

        elif status == "Accepted":
            accepted += 1

        elif status == "Rejected":
            rejected += 1

        elif status == "Cancelled":
            cancelled += 1

    print_title("APPOINTMENT STATUS REPORT")

    print(f"Pending Appointments   : {pending}")
    print(f"Accepted Appointments  : {accepted}")
    print(f"Rejected Appointments  : {rejected}")
    print(f"Cancelled Appointments : {cancelled}")

    line()


# ==========================================================
# Reports Menu
# ==========================================================

def reports_menu():

    while True:

        print_title("REPORTS")

        print("1. Overall Summary")
        print("2. Doctor-wise Appointment Report")
        print("3. Disease-wise Patient Report")
        print("4. Appointment Status Report")
        print("5. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            overall_report()

        elif choice == "2":

            doctor_wise_report()

        elif choice == "3":

            disease_report()

        elif choice == "4":

            appointment_status_report()

        elif choice == "5":

            break

        else:

            print("\nInvalid Choice.")