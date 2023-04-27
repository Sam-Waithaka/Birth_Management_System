import tkinter as tk
import mysql.connector

# Establish connection to the database
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234567890",
        database="birth_management"
    )

# Create a cursor object
mycursor = mydb.cursor()

# Create the doctor screen
class DoctorScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Create a label for the doctor screen
        label = tk.Label(self, text="Doctor Screen", font=("Arial", 18))
        label.pack(pady=10)

        # Create a text area for the doctor to take notes
        notes_label = tk.Label(self, text="Notes:")
        notes_label.pack(pady=5)
        self.notes_text = tk.Text(self, height=5, width=30)
        self.notes_text.pack()

        # Create a button to view pending appointments
        view_appointments_button = tk.Button(self, text="View Pending Appointments", command=self.view_appointments)
        view_appointments_button.pack(pady=10)

    # Function to view pending appointments
    def view_appointments(self):
        # Clear the notes text area
        self.notes_text.delete("1.0", "end")

        # Retrieve the pending appointments from the database
        mycursor.execute("SELECT * FROM appointment WHERE status='Pending'")
        appointments = mycursor.fetchall()

        # Create a label to display the pending appointments
        appointments_label = tk.Label(self, text="Pending Appointments", font=("Arial", 14))
        appointments_label.pack(pady=10)

        # Create a text area to display the pending appointments
        appointments_text = tk.Text(self, height=10, width=50)
        appointments_text.pack()

        # Insert the pending appointments into the text area
        for appointment in appointments:
            appointments_text.insert("end", "Appointment ID: " + str(appointment[0]) + "\n")
            appointments_text.insert("end", "Patient ID: " + str(appointment[1]) + "\n")
            appointments_text.insert("end", "Appointment Date: " + str(appointment[2]) + "\n")
            appointments_text.insert("end", "Appointment Time: " + str(appointment[3]) + "\n")
            appointments_text.insert("end", "Appointment Type: " + str(appointment[4]) + "\n\n")

        # Create a button to select an appointment
        select_appointment_button = tk.Button(self, text="Select Appointment", command=lambda: self.select_appointment(appointments_text.get("1.0", "end-1c")))
        select_appointment_button.pack(pady=10)

    # Function to select an appointment
    def select_appointment(self, appointment_text):
        # Parse the appointment ID from the text
        appointment_id = int(appointment_text.split(": ")[1])

        # Retrieve the patient ID and name from the database
        mycursor.execute("SELECT patient.patient_id, patient.name FROM patient INNER JOIN appointment ON patient.patient_id=appointment.patient_id WHERE appointment.appointment_id=%s", (appointment_id,))
        patient = mycursor.fetchone()

        # Display the patient ID and name
        patient_label = tk.Label(self, text="Patient ID: " + str(patient[0]) + " | Name: " + patient[1], font=("Arial", 14))
        patient_label.pack(pady=10)

        # Create a button to save the notes
        save_notes_button = tk.Button(self, text="Save Notes", command=lambda: self.save_notes(patient[0]))
        save_notes_button

# Create a Tk instance
root = tk.Tk()

# Create an instance of the DoctorScreen class
doctor_screen = DoctorScreen(root)

# Display the DoctorScreen on the screen
doctor_screen.pack()

# Run the main event loop
root.mainloop()
