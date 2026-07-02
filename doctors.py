"""
=========================================================
Hospital Appointment Booking System
Doctor Module
=========================================================
"""

from data import doctors
from utils import print_title, line


# =========================================================
# View All Doctors
# =========================================================

def view_doctors():

    if not doctors:
        print("\nNo doctors available.")
        return

    print_title("AVAILABLE DOCTORS")

    for doctor in doctors:

        print(f"Doctor ID       : {doctor['id']}")
        print(f"Name            : {doctor['name']}")
        print(f"Specialization  : {doctor['specialization']}")
        print(f"Available Time  : {doctor['timing']}")

        line()


# =========================================================
# Search Doctor by ID
# =========================================================

def search_doctor_by_id():

    if not doctors:
        print("\nNo doctors available.")
        return

    try:
        doctor_id = int(input("\nEnter Doctor ID : "))
    except ValueError:
        print("Invalid Doctor ID.")
        return

    for doctor in doctors:

        if doctor["id"] == doctor_id:

            print_title("DOCTOR FOUND")

            print(f"Doctor ID       : {doctor['id']}")
            print(f"Name            : {doctor['name']}")
            print(f"Specialization  : {doctor['specialization']}")
            print(f"Available Time  : {doctor['timing']}")

            return

    print("\nDoctor Not Found.")


# =========================================================
# Search Doctor by Name
# =========================================================

def search_doctor_by_name():

    if not doctors:
        print("\nNo doctors available.")
        return

    name = input("\nEnter Doctor Name : ").strip().lower()

    found = False

    print_title("SEARCH RESULT")

    for doctor in doctors:

        if name in doctor["name"].lower():

            found = True

            print(f"Doctor ID       : {doctor['id']}")
            print(f"Name            : {doctor['name']}")
            print(f"Specialization  : {doctor['specialization']}")
            print(f"Available Time  : {doctor['timing']}")

            line()

    if not found:
        print("Doctor Not Found.")


# =========================================================
# Search Doctor by Specialization
# =========================================================

def search_doctor_by_specialization():

    if not doctors:
        print("\nNo doctors available.")
        return

    specialization = input("\nEnter Specialization : ").strip().lower()

    found = False

    print_title("SEARCH RESULT")

    for doctor in doctors:

        if specialization in doctor["specialization"].lower():

            found = True

            print(f"Doctor ID       : {doctor['id']}")
            print(f"Name            : {doctor['name']}")
            print(f"Specialization  : {doctor['specialization']}")
            print(f"Available Time  : {doctor['timing']}")

            line()

    if not found:
        print("No doctor found with that specialization.")


# =========================================================
# View Doctors by Specialization
# =========================================================

def view_specializations():

    if not doctors:
        print("\nNo doctors available.")
        return

    print_title("AVAILABLE SPECIALIZATIONS")

    specializations = []

    for doctor in doctors:

        if doctor["specialization"] not in specializations:

            specializations.append(doctor["specialization"])

    for index, specialization in enumerate(specializations, start=1):

        print(f"{index}. {specialization}")


# =========================================================
# Doctor Menu
# =========================================================

def doctor_menu():

    while True:

        print_title("DOCTOR MANAGEMENT")

        print("1. View All Doctors")
        print("2. Search Doctor by ID")
        print("3. Search Doctor by Name")
        print("4. Search by Specialization")
        print("5. View Specializations")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            view_doctors()

        elif choice == "2":
            search_doctor_by_id()

        elif choice == "3":
            search_doctor_by_name()

        elif choice == "4":
            search_doctor_by_specialization()

        elif choice == "5":
            view_specializations()

        elif choice == "6":
            break

        else:
            print("\nInvalid Choice.")