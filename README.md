# Hospital Appointment Management System

A modular Python application for managing hospital appointments, patient records, doctor information, and appointment scheduling. The project demonstrates the use of Python programming concepts such as modular programming, file handling, JSON storage, lists, dictionaries, functions, and CRUD operations.

---

## Overview

The Hospital Appointment Management System is a console-based application designed to simplify the appointment booking process in hospitals and clinics.

The system allows users to:

- Register and manage patient records
- View and search doctors
- Book appointments
- Accept, reject, or cancel appointments
- Generate summary reports
- Store data using JSON files for persistence

This project was developed as a Python minor project to demonstrate practical implementation of core programming concepts.

---

## Features

### Patient Management

- Add new patients
- View all patients
- Search patient by ID
- Update patient details
- Delete patient records
- Automatic Patient ID generation

### Doctor Management

- View available doctors
- Search doctor by specialization

### Appointment Management

- Book appointments
- Prevent duplicate appointments
- View appointment details
- Accept appointments
- Reject appointments
- Cancel appointments
- Appointment status management

### Reports

- Total patients
- Total doctors
- Total appointments
- Pending appointments
- Accepted appointments
- Rejected appointments
- Cancelled appointments

---

## Technologies Used

- Python 3
- JSON
- Visual Studio Code
- Git
- GitHub

---

## Python Concepts Used

- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- JSON Handling
- CRUD Operations
- Modular Programming
- Input Validation

---

## Project Structure

```
hospital-appointment-management-system/
│
├── appointments.py
├── appointments.json
├── data.py
├── doctors.py
├── main.py
├── patients.py
├── patients.json
├── reports.py
├── utils.py
├── README.md
├── .gitignore
└── Screenshots/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/hospital-appointment-management-system.git
```

### Navigate to the project folder

```bash
cd hospital-appointment-management-system
```

### Run the application

```bash
python main.py
```

---

## Sample Workflow

```
Main Menu
│
├── Patient Management
│     ├── Add Patient
│     ├── View Patients
│     ├── Search Patient
│     ├── Update Patient
│     └── Delete Patient
│
├── Doctor Management
│     ├── View Doctors
│     └── Search Doctor
│
├── Appointment Management
│     ├── Book Appointment
│     ├── View Appointment
│     ├── Accept / Reject
│     └── Cancel Appointment
│
└── Reports
```

---

## Data Storage

The application stores information locally using JSON files.

```
patients.json
appointments.json
```

These files automatically save patient and appointment information, allowing data to persist between program executions.

---

## Screenshots

The `Screenshots` folder contains sample outputs of the application, including:

- Main Menu
- Add Patient
- Patient List
- Doctor List
- Appointment Booking
- Reports

---

## Future Improvements

Some features that can be added in future versions include:

- Graphical User Interface (Tkinter or PyQt)
- Login and Authentication
- Doctor Management Module
- MySQL Database Integration
- Email Notifications
- SMS Appointment Alerts
- PDF Report Generation
- Web-based Version using Flask or Django
- REST API Support

---

## Learning Outcomes

This project helped in understanding:

- Modular application development
- Python file handling
- JSON-based data persistence
- CRUD operations
- Input validation
- Exception handling
- Console application design

---

## Author

**Shaik Mahammad Muqhthaar Ahmad**

B.Tech – Computer Science and Engineering

Specialization in Artificial Intelligence, Machine Learning & Data Science

---

## License

This project is intended for educational and learning purposes.

---

If you found this project useful, consider giving the repository a star.
