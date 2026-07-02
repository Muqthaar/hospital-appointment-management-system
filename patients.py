"""
=========================================================
Hospital Appointment Booking System
Patient Module
=========================================================
"""

from data import patients, save_data, PATIENT_FILE
from utils import (
    validate_age,
    validate_phone,
    print_title,
    line
)


# ==========================================================
# Generate Patient ID
# ==========================================================

def generate_patient_id():

    if not patients:
        return 101

    return patients[-1]["id"] + 1


# ==========================================================
# Add Patient
# ==========================================================

def add_patient():

    print_title("ADD NEW PATIENT")

    # ---------------- Name ----------------

    while True:

        name = input("Enter Patient Name : ").strip()

        if name:
            break

        print("Name cannot be empty.")

    # ---------------- Age ----------------

    while True:

        try:

            age = int(input("Enter Age : "))

            if validate_age(age):
                break

            print("Age must be between 1 and 120.")

        except ValueError:

            print("Please enter a valid number.")

    # ---------------- Gender ----------------

    while True:

        gender = input(
            "Enter Gender (Male/Female/Other) : "
        ).strip().title()

        if gender in ["Male", "Female", "Other"]:
            break

        print("Invalid Gender.")

    # ---------------- Phone ----------------

    while True:

        phone = input("Enter Phone Number : ").strip()

        if not validate_phone(phone):

            print("Phone number must contain exactly 10 digits.")
            continue

        duplicate = False

        for patient in patients:

            if patient["phone"] == phone:

                duplicate = True
                break

        if duplicate:

            print("Phone number already exists.")

        else:

            break

    # ---------------- Disease ----------------

    while True:

        disease = input("Enter Disease : ").strip()

        if disease:
            break

        print("Disease cannot be empty.")

    patient = {

        "id": generate_patient_id(),

        "name": name,

        "age": age,

        "gender": gender,

        "phone": phone,

        "disease": disease

    }

    patients.append(patient)

    save_data(PATIENT_FILE, patients)

    print("\nPatient Added Successfully.")

    print(f"Generated Patient ID : {patient['id']}")


# ==========================================================
# View Patients
# ==========================================================

def view_patients():

    if not patients:

        print("\nNo patients available.")

        return

    print_title("PATIENT LIST")

    for patient in patients:

        print(f"Patient ID : {patient['id']}")
        print(f"Name       : {patient['name']}")
        print(f"Age        : {patient['age']}")
        print(f"Gender     : {patient['gender']}")
        print(f"Phone      : {patient['phone']}")
        print(f"Disease    : {patient['disease']}")

        line()


# ==========================================================
# Search Patient By ID
# ==========================================================

def search_patient_by_id():

    if not patients:

        print("\nNo patients available.")

        return

    try:

        patient_id = int(input("\nEnter Patient ID : "))

    except ValueError:

        print("Invalid Patient ID.")

        return

    for patient in patients:

        if patient["id"] == patient_id:

            print_title("PATIENT FOUND")

            print(f"Patient ID : {patient['id']}")
            print(f"Name       : {patient['name']}")
            print(f"Age        : {patient['age']}")
            print(f"Gender     : {patient['gender']}")
            print(f"Phone      : {patient['phone']}")
            print(f"Disease    : {patient['disease']}")

            return

    print("\nPatient Not Found.")


# ==========================================================
# Search Patient By Name
# ==========================================================

def search_patient_by_name():

    if not patients:

        print("\nNo patients available.")

        return

    keyword = input("\nEnter Patient Name : ").strip().lower()

    found = False

    print_title("SEARCH RESULT")

    for patient in patients:

        if keyword in patient["name"].lower():

            found = True

            print(f"Patient ID : {patient['id']}")
            print(f"Name       : {patient['name']}")
            print(f"Age        : {patient['age']}")
            print(f"Gender     : {patient['gender']}")
            print(f"Phone      : {patient['phone']}")
            print(f"Disease    : {patient['disease']}")

            line()

    if not found:

        print("Patient Not Found.")

# ==========================================================
# Update Patient
# ==========================================================

def update_patient():

    if not patients:
        print("\nNo patients available.")
        return

    try:
        patient_id = int(input("\nEnter Patient ID : "))
    except ValueError:
        print("Invalid Patient ID.")
        return

    for patient in patients:

        if patient["id"] == patient_id:

            while True:

                print_title("UPDATE PATIENT")

                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Gender")
                print("4. Update Phone")
                print("5. Update Disease")
                print("6. Back")

                choice = input("\nEnter Choice : ")

                if choice == "1":

                    while True:

                        name = input("Enter New Name : ").strip()

                        if name:
                            patient["name"] = name
                            break

                        print("Name cannot be empty.")

                elif choice == "2":

                    while True:

                        try:

                            age = int(input("Enter New Age : "))

                            if validate_age(age):

                                patient["age"] = age
                                break

                            print("Age must be between 1 and 120.")

                        except ValueError:

                            print("Enter a valid number.")

                elif choice == "3":

                    while True:

                        gender = input(
                            "Enter Gender (Male/Female/Other) : "
                        ).strip().title()

                        if gender in ["Male", "Female", "Other"]:

                            patient["gender"] = gender
                            break

                        print("Invalid Gender.")

                elif choice == "4":

                    while True:

                        phone = input("Enter New Phone : ").strip()

                        if not validate_phone(phone):

                            print("Phone number must contain exactly 10 digits.")
                            continue

                        duplicate = False

                        for p in patients:

                            if p["phone"] == phone and p["id"] != patient["id"]:

                                duplicate = True
                                break

                        if duplicate:

                            print("Phone number already exists.")

                        else:

                            patient["phone"] = phone
                            break

                elif choice == "5":

                    while True:

                        disease = input("Enter New Disease : ").strip()

                        if disease:

                            patient["disease"] = disease
                            break

                        print("Disease cannot be empty.")

                elif choice == "6":

                    return

                else:

                    print("Invalid Choice.")
                    continue

                save_data(PATIENT_FILE, patients)

                print("\nPatient Updated Successfully.")

                return

    print("\nPatient Not Found.")


# ==========================================================
# Delete Patient
# ==========================================================

def delete_patient():

    if not patients:

        print("\nNo patients available.")
        return

    try:

        patient_id = int(input("\nEnter Patient ID : "))

    except ValueError:

        print("Invalid Patient ID.")
        return

    for patient in patients:

        if patient["id"] == patient_id:

            confirm = input(
                f"\nDelete patient '{patient['name']}'? (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                patients.remove(patient)

                save_data(PATIENT_FILE, patients)

                print("\nPatient Deleted Successfully.")

            else:

                print("\nDeletion Cancelled.")

            return

    print("\nPatient Not Found.")


# ==========================================================
# Patient Menu
# ==========================================================

def patient_menu():

    while True:

        print_title("PATIENT MANAGEMENT")

        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient by ID")
        print("4. Search Patient by Name")
        print("5. Update Patient")
        print("6. Delete Patient")
        print("7. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_patient()

        elif choice == "2":

            view_patients()

        elif choice == "3":

            search_patient_by_id()

        elif choice == "4":

            search_patient_by_name()

        elif choice == "5":

            update_patient()

        elif choice == "6":

            delete_patient()

        elif choice == "7":

            break

        else:

            print("\nInvalid Choice.")