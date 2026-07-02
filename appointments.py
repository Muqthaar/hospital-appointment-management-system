"""
=========================================================
Hospital Appointment Booking System
Appointment Module
=========================================================
"""

from datetime import datetime

from data import (
    appointments,
    patients,
    doctors,
    save_data,
    APPOINTMENT_FILE
)

from utils import (
    validate_date,
    validate_time,
    is_future_date,
    print_title,
    line
)


# ==========================================================
# Generate Appointment ID
# ==========================================================

def generate_appointment_id():

    if not appointments:
        return "APT1001"

    last_id = appointments[-1]["appointment_id"]

    number = int(last_id.replace("APT", ""))

    return f"APT{number + 1}"


# ==========================================================
# Book Appointment
# ==========================================================

def book_appointment():

    if not patients:

        print("\nNo patients available.")
        return

    if not doctors:

        print("\nNo doctors available.")
        return

    print_title("AVAILABLE PATIENTS")

    for patient in patients:

        print(f"{patient['id']} - {patient['name']}")

    try:

        patient_id = int(input("\nEnter Patient ID : "))

    except ValueError:

        print("Invalid Patient ID.")
        return

    patient_exists = False

    for patient in patients:

        if patient["id"] == patient_id:

            patient_exists = True
            break

    if not patient_exists:

        print("Patient Not Found.")
        return

    print_title("AVAILABLE DOCTORS")

    for doctor in doctors:

        print(
            f"{doctor['id']} - "
            f"{doctor['name']} "
            f"({doctor['specialization']})"
        )

    try:

        doctor_id = int(input("\nEnter Doctor ID : "))

    except ValueError:

        print("Invalid Doctor ID.")
        return

    doctor_exists = False

    for doctor in doctors:

        if doctor["id"] == doctor_id:

            doctor_exists = True
            break

    if not doctor_exists:

        print("Doctor Not Found.")
        return

    while True:

        date = input(
            "Enter Appointment Date (DD-MM-YYYY): "
        )

        if not validate_date(date):

            print("Invalid Date Format.")
            continue

        if not is_future_date(date):

            print("Past dates are not allowed.")
            continue

        break

    while True:

        time = input(
            "Enter Appointment Time (HH:MM AM/PM): "
        )

        if validate_time(time):
            break

        print("Invalid Time Format.")

    for appointment in appointments:

        if (
            appointment["patient_id"] == patient_id
            and appointment["doctor_id"] == doctor_id
            and appointment["date"] == date
            and appointment["time"] == time
        ):

            print("\nDuplicate Appointment Found.")

            return

    appointment = {

        "appointment_id": generate_appointment_id(),

        "patient_id": patient_id,

        "doctor_id": doctor_id,

        "date": date,

        "time": time,

        "status": "Pending",

        "booked_on": datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    }

    appointments.append(appointment)

    save_data(APPOINTMENT_FILE, appointments)

    print("\nAppointment Booked Successfully.")

    print(
        f"Appointment ID : "
        f"{appointment['appointment_id']}"
    )


# ==========================================================
# View Appointments
# ==========================================================

def view_appointments():

    if not appointments:

        print("\nNo appointments available.")
        return

    print_title("APPOINTMENT DETAILS")

    for appointment in appointments:

        patient_name = "Unknown"

        doctor_name = "Unknown"

        for patient in patients:

            if patient["id"] == appointment["patient_id"]:

                patient_name = patient["name"]
                break

        for doctor in doctors:

            if doctor["id"] == appointment["doctor_id"]:

                doctor_name = doctor["name"]
                break

        print(
            f"Appointment ID : "
            f"{appointment['appointment_id']}"
        )

        print(f"Patient Name   : {patient_name}")

        print(f"Doctor Name    : {doctor_name}")

        print(f"Date           : {appointment['date']}")

        print(f"Time           : {appointment['time']}")

        print(f"Status         : {appointment['status']}")

        print(
            f"Booked On      : "
            f"{appointment['booked_on']}"
        )

        line()

# ==========================================================
# Search Appointment by ID
# ==========================================================

def search_appointment():

    if not appointments:

        print("\nNo appointments available.")
        return

    appointment_id = input(
        "\nEnter Appointment ID : "
    ).strip().upper()

    for appointment in appointments:

        if appointment["appointment_id"] == appointment_id:

            patient_name = "Unknown"
            doctor_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print_title("APPOINTMENT FOUND")

            print(
                f"Appointment ID : "
                f"{appointment['appointment_id']}"
            )

            print(f"Patient Name   : {patient_name}")

            print(f"Doctor Name    : {doctor_name}")

            print(f"Date           : {appointment['date']}")

            print(f"Time           : {appointment['time']}")

            print(f"Status         : {appointment['status']}")

            print(
                f"Booked On      : "
                f"{appointment['booked_on']}"
            )

            return

    print("\nAppointment Not Found.")


# ==========================================================
# View Appointments by Patient
# ==========================================================

def view_patient_appointments():

    if not appointments:

        print("\nNo appointments available.")
        return

    try:

        patient_id = int(input("\nEnter Patient ID : "))

    except ValueError:

        print("Invalid Patient ID.")
        return

    found = False

    print_title("PATIENT APPOINTMENTS")

    for appointment in appointments:

        if appointment["patient_id"] == patient_id:

            found = True

            doctor_name = "Unknown"

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print(
                f"Appointment ID : "
                f"{appointment['appointment_id']}"
            )

            print(f"Doctor         : {doctor_name}")

            print(f"Date           : {appointment['date']}")

            print(f"Time           : {appointment['time']}")

            print(f"Status         : {appointment['status']}")

            line()

    if not found:

        print("No appointments found.")


# ==========================================================
# View Appointments by Doctor
# ==========================================================

def view_doctor_appointments():

    if not appointments:

        print("\nNo appointments available.")
        return

    try:

        doctor_id = int(input("\nEnter Doctor ID : "))

    except ValueError:

        print("Invalid Doctor ID.")
        return

    found = False

    print_title("DOCTOR APPOINTMENTS")

    for appointment in appointments:

        if appointment["doctor_id"] == doctor_id:

            found = True

            patient_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            print(
                f"Appointment ID : "
                f"{appointment['appointment_id']}"
            )

            print(f"Patient        : {patient_name}")

            print(f"Date           : {appointment['date']}")

            print(f"Time           : {appointment['time']}")

            print(f"Status         : {appointment['status']}")

            line()

    if not found:

        print("No appointments found.")


# ==========================================================
# Get Appointment Object
# ==========================================================

def get_appointment(appointment_id):

    for appointment in appointments:

        if appointment["appointment_id"] == appointment_id:

            return appointment

    return None

# ==========================================================
# Accept / Reject Appointment
# ==========================================================

def answer_appointment():

    if not appointments:

        print("\nNo appointments available.")
        return

    appointment_id = input(
        "\nEnter Appointment ID : "
    ).strip().upper()

    appointment = get_appointment(appointment_id)

    if appointment is None:

        print("\nAppointment Not Found.")
        return

    if appointment["status"] == "Cancelled":

        print("\nCancelled appointments cannot be updated.")
        return

    print("\nCurrent Status :", appointment["status"])

    print("\n1. Accept")
    print("2. Reject")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        appointment["status"] = "Accepted"

    elif choice == "2":

        appointment["status"] = "Rejected"

    else:

        print("Invalid Choice.")
        return

    save_data(APPOINTMENT_FILE, appointments)

    print("\nAppointment Updated Successfully.")


# ==========================================================
# Cancel Appointment
# ==========================================================

def cancel_appointment():

    if not appointments:

        print("\nNo appointments available.")
        return

    appointment_id = input(
        "\nEnter Appointment ID : "
    ).strip().upper()

    appointment = get_appointment(appointment_id)

    if appointment is None:

        print("\nAppointment Not Found.")
        return

    if appointment["status"] == "Cancelled":

        print("\nAppointment is already cancelled.")
        return

    confirm = input(
        "\nAre you sure you want to cancel? (Y/N): "
    ).strip().upper()

    if confirm != "Y":

        print("\nCancellation Cancelled.")
        return

    appointment["status"] = "Cancelled"

    save_data(APPOINTMENT_FILE, appointments)

    print("\nAppointment Cancelled Successfully.")


# ==========================================================
# View Pending Appointments
# ==========================================================

def view_pending_appointments():

    found = False

    print_title("PENDING APPOINTMENTS")

    for appointment in appointments:

        if appointment["status"] == "Pending":

            found = True

            patient_name = "Unknown"
            doctor_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print(f"Appointment ID : {appointment['appointment_id']}")
            print(f"Patient        : {patient_name}")
            print(f"Doctor         : {doctor_name}")
            print(f"Date           : {appointment['date']}")
            print(f"Time           : {appointment['time']}")

            line()

    if not found:

        print("No pending appointments.")


# ==========================================================
# View Accepted Appointments
# ==========================================================

def view_accepted_appointments():

    found = False

    print_title("ACCEPTED APPOINTMENTS")

    for appointment in appointments:

        if appointment["status"] == "Accepted":

            found = True

            patient_name = "Unknown"
            doctor_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print(f"Appointment ID : {appointment['appointment_id']}")
            print(f"Patient        : {patient_name}")
            print(f"Doctor         : {doctor_name}")
            print(f"Date           : {appointment['date']}")
            print(f"Time           : {appointment['time']}")

            line()

    if not found:

        print("No accepted appointments.")

# ==========================================================
# View Rejected Appointments
# ==========================================================

def view_rejected_appointments():

    found = False

    print_title("REJECTED APPOINTMENTS")

    for appointment in appointments:

        if appointment["status"] == "Rejected":

            found = True

            patient_name = "Unknown"
            doctor_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print(f"Appointment ID : {appointment['appointment_id']}")
            print(f"Patient        : {patient_name}")
            print(f"Doctor         : {doctor_name}")
            print(f"Date           : {appointment['date']}")
            print(f"Time           : {appointment['time']}")

            line()

    if not found:

        print("No rejected appointments.")


# ==========================================================
# View Cancelled Appointments
# ==========================================================

def view_cancelled_appointments():

    found = False

    print_title("CANCELLED APPOINTMENTS")

    for appointment in appointments:

        if appointment["status"] == "Cancelled":

            found = True

            patient_name = "Unknown"
            doctor_name = "Unknown"

            for patient in patients:

                if patient["id"] == appointment["patient_id"]:

                    patient_name = patient["name"]
                    break

            for doctor in doctors:

                if doctor["id"] == appointment["doctor_id"]:

                    doctor_name = doctor["name"]
                    break

            print(f"Appointment ID : {appointment['appointment_id']}")
            print(f"Patient        : {patient_name}")
            print(f"Doctor         : {doctor_name}")
            print(f"Date           : {appointment['date']}")
            print(f"Time           : {appointment['time']}")

            line()

    if not found:

        print("No cancelled appointments.")


# ==========================================================
# Appointment Menu
# ==========================================================

def appointment_menu():

    while True:

        print_title("APPOINTMENT MANAGEMENT")

        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Search Appointment")
        print("4. View Patient Appointments")
        print("5. View Doctor Appointments")
        print("6. Accept / Reject Appointment")
        print("7. Cancel Appointment")
        print("8. View Pending Appointments")
        print("9. View Accepted Appointments")
        print("10. View Rejected Appointments")
        print("11. View Cancelled Appointments")
        print("12. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            book_appointment()

        elif choice == "2":

            view_appointments()

        elif choice == "3":

            search_appointment()

        elif choice == "4":

            view_patient_appointments()

        elif choice == "5":

            view_doctor_appointments()

        elif choice == "6":

            answer_appointment()

        elif choice == "7":

            cancel_appointment()

        elif choice == "8":

            view_pending_appointments()

        elif choice == "9":

            view_accepted_appointments()

        elif choice == "10":

            view_rejected_appointments()

        elif choice == "11":

            view_cancelled_appointments()

        elif choice == "12":

            break

        else:

            print("\nInvalid Choice.")