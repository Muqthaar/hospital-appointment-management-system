import json
import os

# ==========================================================
# JSON File Names
# ==========================================================

PATIENT_FILE = "patients.json"
APPOINTMENT_FILE = "appointments.json"

# ==========================================================
# Doctors Database (Fixed Data)
# ==========================================================

doctors = [
    {
        "id": 1,
        "name": "Dr. Amit Sharma",
        "specialization": "General Physician",
        "timing": "09:00 AM - 12:00 PM"
    },
    {
        "id": 2,
        "name": "Dr. Priya Singh",
        "specialization": "Cardiologist",
        "timing": "10:00 AM - 01:00 PM"
    },
    {
        "id": 3,
        "name": "Dr. Rajesh Kumar",
        "specialization": "Orthopedic",
        "timing": "02:00 PM - 05:00 PM"
    },
    {
        "id": 4,
        "name": "Dr. Neha Verma",
        "specialization": "Dermatologist",
        "timing": "11:00 AM - 03:00 PM"
    },
    {
        "id": 5,
        "name": "Dr. Arjun Patel",
        "specialization": "Neurologist",
        "timing": "04:00 PM - 07:00 PM"
    },
    {
        "id": 6,
        "name": "Dr. Sneha Rao",
        "specialization": "Pediatrician",
        "timing": "09:00 AM - 11:00 AM"
    },
    {
        "id": 7,
        "name": "Dr. Vikram Mehta",
        "specialization": "ENT Specialist",
        "timing": "01:00 PM - 04:00 PM"
    },
    {
        "id": 8,
        "name": "Dr. Anjali Gupta",
        "specialization": "Gynecologist",
        "timing": "10:00 AM - 02:00 PM"
    }
]

# ==========================================================
# Create JSON Files Automatically
# ==========================================================

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=4)

create_file(PATIENT_FILE)
create_file(APPOINTMENT_FILE)

# ==========================================================
# Load Data
# ==========================================================

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ==========================================================
# Save Data
# ==========================================================

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# ==========================================================
# Load Patients & Appointments
# ==========================================================

patients = load_data(PATIENT_FILE)
appointments = load_data(APPOINTMENT_FILE)