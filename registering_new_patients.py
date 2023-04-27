import mysql.connector
from tkinter import *

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="birth_management"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Define a function to save the patient information to the database
def save_patient():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = dob_entry.get()
    address = address_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    medical_history = history_entry.get()
    insurance_information = insurance_entry.get()

    # Execute the SQL query to insert the patient information into the database
    sql = "INSERT INTO Patient (first_name, last_name, date_of_birth, address, phone_number, email, medical_history, " \
          "insurance_information) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, date_of_birth, address, phone_number, email, medical_history, insurance_information)
    mycursor.execute(sql, val)
    mydb.commit()

    # Print a success message
    print(mycursor.rowcount, "record inserted.")

# Create a Tkinter window
root = Tk()
root.title("Patient Registration")

# Create form labels and entry fields
first_name_label = Label(root, text="First Name:")
first_name_label.grid(row=0, column=0)
first_name_entry = Entry(root)
first_name_entry.grid(row=0, column=1)

last_name_label = Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0)
last_name_entry = Entry(root)
last_name_entry.grid(row=1, column=1)

dob_label = Label(root, text="Date of Birth:")
dob_label.grid(row=2, column=0)
dob_entry = Entry(root)
dob_entry.grid(row=2, column=1)

address_label = Label(root, text="Address:")
address_label.grid(row=3, column=0)
address_entry = Entry(root)
address_entry.grid(row=3, column=1)

phone_label = Label(root, text="Phone Number:")
phone_label.grid(row=4, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=4, column=1)

email_label = Label(root, text="Email:")
email_label.grid(row=5, column=0)
email_entry = Entry(root)
email_entry.grid(row=5, column=1)

history_label = Label(root, text="Medical History:")
history_label.grid(row=6, column=0)
history_entry = Entry(root)
history_entry.grid(row=6, column=1)

insurance_label = Label(root, text="Insurance Information:")
insurance_label.grid(row=7, column=0)
insurance_entry = Entry(root)
insurance_entry.grid(row=7, column=1)

# Create a button to save the patient information
save_button = Button(root, text="Save", command=save_patient)
save_button.grid(row=8, column=1)

# Start the Tkinter event loop
root.mainloop()
