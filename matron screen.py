import tkinter as tk
import mysql.connector

import appointments
import doctor_screen
import registering_new_patients

# Establish connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="birth_management"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create the Matron screen
class AppointmentsScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Create a label for the Appointments screen
        label = tk.Label(self, text="Appointments Screen", font=("Arial", 18))
        label.pack(pady=10)

        # Create a button to return to the Matron screen
        return_button = tk.Button(self, text="Back", command=lambda: self.__init__(self.parent))
        return_button.pack(pady=10)

class MatronScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Create a label for the Matron screen
        label = tk.Label(self, text="Matron Screen", font=("Arial", 18))
        label.pack(pady=10)

        # Create buttons to view the contents of each table in the database
        view_doctors_button = tk.Button(self, text="View Doctors", command=lambda: doctor_screen.py(self.parent),state="normal")
        view_doctors_button.pack(pady=10)

        view_patients_button = tk.Button(self, text="View Patients", command=lambda: doctor_screen.py(self.parent),state="normal")
        view_patients_button.pack(pady=10)

        view_appointments_button = tk.Button(self, text="View Appointments", command=lambda: AppointmentsScreen(self.parent), state="normal")
        view_appointments_button.pack(pady=10)

        view_babies_button = tk.Button(self, text="View Babies", command=lambda: (registering_new_patients.py)(self.parent),state="normal")
        view_babies_button.pack(pady=10)

        # Disable editing functionality in the GUI
        # self.disable_editing()

    # Function to view the contents of a table in the database
    def view_table(self, table_name):
        # Clear the screen
        for widget in self.winfo_children():
            widget.destroy()

        # Retrieve the contents of the table from the database
        mycursor.execute(f"SELECT * FROM {table_name}")
        table_contents = mycursor.fetchall()

        # Create a label to display the table name
        table_label = tk.Label(self, text=table_name.capitalize() + "s", font=("Arial", 14))
        table_label.pack(pady=10)

        # Create a text area to display the table contents
        table_text = tk.Text(self, height=10, width=50)
        table_text.pack()

        # Insert the table contents into the text area
        for row in table_contents:
            table_text.insert("end", str(row) + "\n")

        # Create a button to return to the Matron screen
        return_button = tk.Button(self, text="Back", command=lambda: self.__init__(self.parent))
        return_button.pack(pady=10)

    # Function to disable editing functionality in the GUI
    # def disable_editing(self):
    #     for widget in self.winfo_children():
    #         if isinstance(widget, tk.Entry) or isinstance(widget, tk.Text):
    #             widget.configure(state="disabled")
    #         elif isinstance(widget, tk.Button):
    #             widget.configure(state="disabled")

# Create a tkinter root window
root = tk.Tk()

# Create an instance of the MatronScreen class and pack it into the root window
matron_screen = MatronScreen(root)
matron_screen.pack(fill="both", expand=True)

# Start the tkinter event loop
root.mainloop()
