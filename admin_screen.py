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

# Create the Admin screen
class AdminScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Create a label for the Admin screen
        label = tk.Label(self, text="Admin Screen", font=("Arial", 18))
        label.pack(pady=10)

        # Create buttons to view, add, update, and delete records in each table in the database
        view_doctors_button = tk.Button(self, text="View Doctors", command=lambda: self.view_table("doctor"))
        view_doctors_button.pack(pady=10)

        add_doctor_button = tk.Button(self, text="Add Doctor", command=lambda: self.add_record("doctor"))
        add_doctor_button.pack(pady=10)

        update_doctor_button = tk.Button(self, text="Update Doctor", command=lambda: self.update_record("doctor"))
        update_doctor_button.pack(pady=10)

        delete_doctor_button = tk.Button(self, text="Delete Doctor", command=lambda: self.delete_record("doctor"))
        delete_doctor_button.pack(pady=10)

        view_patients_button = tk.Button(self, text="View Patients", command=lambda: self.view_table("patient"))
        view_patients_button.pack(pady=10)

        add_patient_button = tk.Button(self, text="Add Patient", command=lambda: self.add_record("patient"))
        add_patient_button.pack(pady=10)

        update_patient_button = tk.Button(self, text="Update Patient", command=lambda: self.update_record("patient"))
        update_patient_button.pack(pady=10)

        delete_patient_button = tk.Button(self, text="Delete Patient", command=lambda: self.delete_record("patient"))
        delete_patient_button.pack(pady=10)

        view_appointments_button = tk.Button(self, text="View Appointments", command=lambda: self.view_table("appointment"))
        view_appointments_button.pack(pady=10)

        add_appointment_button = tk.Button(self, text="Add Appointment", command=lambda: self.add_record("appointment"))
        add_appointment_button.pack(pady=10)

        update_appointment_button = tk.Button(self, text="Update Appointment", command=lambda: self.update_record("appointment"))
        update_appointment_button.pack(pady=10)

        delete_appointment_button = tk.Button(self, text="Delete Appointment", command=lambda: self.delete_record("appointment"))
        delete_appointment_button.pack(pady=10)

        view_babies_button = tk.Button(self, text="View Babies", command=lambda: self.view_table("baby"))
        view_babies_button.pack(pady=10)

        add_baby_button = tk.Button(self, text="Add Baby", command=lambda: self.add_record("baby"))
        add_baby_button.pack(pady=10)

        update_baby_button = tk.Button(self, text="Update Baby", command=lambda: self.update_record("baby"))
        update_baby_button.pack(pady=10)

        delete_baby_button = tk.Button(self, text="Delete Baby", command=lambda: self.delete_record("baby"))
        delete_baby_button.pack(pady=10)

    # Function to view the contents of a table in the database
    def view_table(self, table_name):
        # Clear the screen
        for widget in self.winfo_children():
            widget.destroy()

        # Get the records from the table
        mycursor.execute

    def view_records(table_name):
        mycursor.execute("SELECT * FROM {}".format(table_name))
        records = mycursor.fetchall()
        # Display the records in a table or list widget in the UI

    def add_record(table_name, values):
        sql = "INSERT INTO {} VALUES {}".format(table_name, values)
        mycursor.execute(sql)
        mydb.commit()
        # Display a message in the UI to indicate the record was added successfully

    def update_record(table_name, record_id, field, new_value):
        sql = "UPDATE {} SET {} = '{}' WHERE id = {}".format(table_name, field, new_value, record_id)
        mycursor.execute(sql)
        mydb.commit()
        # Display a message in the UI to indicate the record was updated successfully

    def delete_record(table_name, record_id):
        sql = "DELETE FROM {} WHERE id = {}".format(table_name, record_id)
        mycursor.execute(sql)
        mydb.commit()
        # Display a message in the UI to indicate the record was deleted successfully

# Create the UI
class App:
    def __init__(self, master):
        self.master = master
        master.title("Birth Management System")

        # Create buttons for each database operation
        view_doctors_button = tk.Button(master, text="View Doctors", command=lambda: view_records("doctor"))
        view_doctors_button.pack()

        add_doctor_button = tk.Button(master, text="Add Doctor", command=lambda: add_record("doctor", values))
        add_doctor_button.pack()

        update_doctor_button = tk.Button(master, text="Update Doctor", command=lambda: update_record("doctor", record_id, field, new_value))
        update_doctor_button.pack()

        delete_doctor_button = tk.Button(master, text="Delete Doctor", command=lambda: delete_record("doctor", record_id))
        delete_doctor_button.pack()

        # Create buttons for other tables as well

        # Define any additional UI elements as needed

# Run the UI
root = tk.Tk()
app = App(root)
root.mainloop()
