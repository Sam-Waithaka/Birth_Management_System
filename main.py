import tkinter as tk
from tkinter import messagebox
import mysql.connector

# create a tkinter window
root = tk.Tk()
root.title("Hospital Management System")

# set the window size
root.geometry("500x300")

# create a label for the email entry box
email_label = tk.Label(root, text="Email")
email_label.pack()

# create an entry box for the email
email_entry = tk.Entry(root)
email_entry.pack()

# create a label for the password entry box
password_label = tk.Label(root, text="Password")
password_label.pack()

# create an entry box for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack()


# create a function to check the login details
def check_login():
    # get the email and password from the entry boxes
    email = email_entry.get()
    password = password_entry.get()

    # connect to the database
    # create the connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234567890",
        database="birth_management"
    )

    # create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # create a cursor object to execute SQL queries
    cursor = mydb.cursor()

    # execute a SELECT statement to retrieve the staff member with the given email and password
    sql = "SELECT * FROM Staff WHERE email = %s AND password = %s"
    val = (email, password)
    cursor.execute(sql, val)

    # fetch the results
    result = cursor.fetchone()

    # check if a staff member was found with the given email and password
    if result is None:
        messagebox.showerror("Error", "Incorrect email or password")
    else:
        # get the role of the staff member
        role = result[2]

        # check if the staff member is a matron
        if role == "admin":
            # Perform admin actions
            messagebox.showinfo("Login Successful", "Welcome Admin!")

        elif role == "doctor":
            # Perform doctor actions
            messagebox.showinfo("Login Successful", "Welcome Doctor!")
            import doctor_screen

        elif role == "nurse":
            # Perform nurse actions
            messagebox.showinfo("Login Successful", "Welcome Nurse!")
            import recording_births

        elif role == "receptionist":
            # Perform receptionist actions
            messagebox.showinfo("Login Successful", "Welcome Receptionist!")
            import reception_screen

        elif role == "matron":
            # Perform matron actions
            messagebox.showinfo("Login Successful", "Welcome Matron!")

        else:
            messagebox.showerror("Login Failed", "Incorrect Password")


    # close the database connection
    mydb.close()


# create a button to submit the login details
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

# start the tkinter event loop
root.mainloop()
