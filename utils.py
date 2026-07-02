"""
=========================================================
Hospital Appointment Booking System
Utility Functions
=========================================================
"""

from datetime import datetime
import os


# =========================================================
# Validate Age
# =========================================================

def validate_age(age):
    """
    Returns True if age is between 1 and 120.
    """
    return 1 <= age <= 120


# =========================================================
# Validate Phone Number
# =========================================================

def validate_phone(phone):
    """
    Phone number must contain exactly 10 digits.
    """
    return phone.isdigit() and len(phone) == 10


# =========================================================
# Validate Date
# =========================================================

def validate_date(date):

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False


# =========================================================
# Validate Time
# =========================================================

def validate_time(time):

    try:
        datetime.strptime(time, "%I:%M %p")
        return True

    except ValueError:
        return False


# =========================================================
# Check Future Date
# =========================================================

def is_future_date(date):

    """
    Returns True if today's date or future date.
    """

    try:

        entered = datetime.strptime(date, "%d-%m-%Y").date()
        today = datetime.today().date()

        return entered >= today

    except ValueError:
        return False


# =========================================================
# Clear Screen
# =========================================================

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# =========================================================
# Pause Screen
# =========================================================

def pause():

    input("\nPress Enter to continue...")


# =========================================================
# Title Printing
# =========================================================

def print_title(title):

    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


# =========================================================
# Separator
# =========================================================

def line():

    print("-" * 70)