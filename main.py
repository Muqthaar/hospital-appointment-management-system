from utils import print_title

from doctors import doctor_menu
from patients import patient_menu
from appointments import appointment_menu
from reports import reports_menu


def main():

    while True:

        print_title("HOSPITAL APPOINTMENT BOOKING SYSTEM")

        print("1. Doctor Management")
        print("2. Patient Management")
        print("3. Appointment Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            doctor_menu()

        elif choice == "2":

            patient_menu()

        elif choice == "3":

            appointment_menu()

        elif choice == "4":

            reports_menu()

        elif choice == "5":

            print("\nThank You!")
            break

        else:

            print("\nInvalid Choice.")


if __name__ == "__main__":
    main()