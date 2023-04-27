import mysql.connector
from tkinter import *

# create the connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="birth_management"
)

# create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# create the main application window using Tkinter
root = Tk()
root.title("Appointment Recording System")
root.geometry("500x500")

# create the appointment recording form
def record_appointment():
    # get the form data
    patient_id = patient_id_entry.get()
    staff_id = staff_id_entry.get()
    appointment_date_time = appointment_date_time_entry.get()
    appointment_duration = appointment_duration_entry.get()
    location = location_entry.get()
    notes = notes_entry.get()

    # insert the appointment into the database
    sql = "INSERT INTO Appointment (patient_id, staff_id, appointment_date_time, appointment_duration, location, notes) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (patient_id, staff_id, appointment_date_time, appointment_duration, location, notes)
    mycursor.execute(sql, val)
    mydb.commit()

    # clear the form fields
    patient_id_entry.delete(0, END)
    staff_id_entry.delete(0, END)
    appointment_date_time_entry.delete(0, END)
    appointment_duration_entry.delete(0, END)
    location_entry.delete(0, END)
    notes_entry.delete(0, END)

    # display a success message
    success_label = Label(root, text="Appointment recorded successfully", fg="green")
    success_label.pack()

# create the form fields
patient_id_label = Label(root, text="Patient ID")
patient_id_label.pack()
patient_id_entry = Entry(root)
patient_id_entry.pack()

staff_id_label = Label(root, text="Staff ID")
staff_id_label.pack()
staff_id_entry = Entry(root)
staff_id_entry.pack()

appointment_date_time_label = Label(root, text="Appointment Date and Time")
appointment_date_time_label.pack()
appointment_date_time_entry = Entry(root)
appointment_date_time_entry.pack()

appointment_duration_label = Label(root, text="Appointment Duration")
appointment_duration_label.pack()
appointment_duration_entry = Entry(root)
appointment_duration_entry.pack()

location_label = Label(root, text="Location")
location_label.pack()
location_entry = Entry(root)
location_entry.pack()

notes_label = Label(root, text="Notes")
notes_label.pack()
notes_entry = Entry(root)
notes_entry.pack()

# create the submit button
submit_button = Button(root, text="Record Appointment", command=record_appointment)
submit_button.pack()

# start the main application loop
root.mainloop()
