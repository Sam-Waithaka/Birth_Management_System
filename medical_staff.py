import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="birth_management"
)

# Create a cursor
mycursor = mydb.cursor()

# Define a function to query the database and display the results in the GUI
def display_medical_staff():
    # Execute the SELECT statement
    mycursor.execute("SELECT * FROM Medical_Staff")
    results = mycursor.fetchall()

    # Clear the treeview widget
    for record in treeview.get_children():
        treeview.delete(record)

    # Insert the results into the treeview widget
    for row in results:
        treeview.insert("", tk.END, values=row)

# Define a function to add a new medical staff member to the database
def add_medical_staff():
    # Get the values from the entry widgets
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    role = entry_role.get()
    specialty = entry_specialty.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()

    # Execute the INSERT statement
    sql = "INSERT INTO Medical_Staff (first_name, last_name, role, specialty, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, role, specialty, phone_number, email)
    mycursor.execute(sql, val)
    mydb.commit()

    # Clear the entry widgets
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_specialty.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    # Refresh the treeview widget
    display_medical_staff()

# Create the GUI
root = tk.Tk()
root.title("Medical Staff")

# Create a treeview widget to display the records
treeview = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), show="headings")
treeview.pack()

# Define the columns of the treeview widget
treeview.heading(1, text="ID")
treeview.column(1, width=50)
treeview.heading(2, text="First Name")
treeview.column(2, width=100)
treeview.heading(3, text="Last Name")
treeview.column(3, width=100)
treeview.heading(4, text="Role")
treeview.column(4, width=150)
treeview.heading(5, text="Specialty")
treeview.column(5, width=150)
treeview.heading(6, text="Email")
treeview.column(6, width=200)

# Populate the treeview widget with the records
display_medical_staff()

# Create a label and entry widget for the first name
label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(root)
entry_first_name.pack()

# Create a label and entry widget for the last name
label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(root)
entry_last_name.pack()

# Create a label and entry widget for the role
label_role = tk.Label(root, text="Role:")
label_role.pack()
entry_role = tk.Entry(root)
entry_role.pack()

# Create a label and entry widget for the specialty
label_specialty = tk.Label(root, text="Specialty:")
label_specialty.pack()
entry_specialty = tk.Entry(root)
entry_specialty.pack()

# Create a label and entry widget for the phone number
label_phone_number = tk.Label(root, text="Phone Number:")
label_phone_number.pack()
entry_phone_number = tk.Entry(root)
entry_phone_number.pack()

# Create a label and entry widget for the email
label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Create a button to add a new medical staff member to the database
button_add = tk.Button(root, text="Add", command=add_medical_staff)
button_add.pack()

root.mainloop()