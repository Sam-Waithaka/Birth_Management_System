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

# Create the GUI
root = tk.Tk()
root.title("Record Birth")

# Create a tab control
tab_control = ttk.Notebook(root)

# Create the Birth Record tab
tab_record_birth = ttk.Frame(tab_control)
tab_control.add(tab_record_birth, text='Record Birth')

# Create labels and entry boxes for the Birth Record tab
label_patient_id = tk.Label(tab_record_birth, text='Patient ID')
entry_patient_id = tk.Entry(tab_record_birth)
label_staff_id = tk.Label(tab_record_birth, text='Staff ID')
entry_staff_id = tk.Entry(tab_record_birth)
label_birth_date_time = tk.Label(tab_record_birth, text='Date and Time of Birth')
entry_birth_date_time = tk.Entry(tab_record_birth)
label_baby_first_name = tk.Label(tab_record_birth, text='Baby First Name')
entry_baby_first_name = tk.Entry(tab_record_birth)
label_baby_last_name = tk.Label(tab_record_birth, text='Baby Last Name')
entry_baby_last_name = tk.Entry(tab_record_birth)
label_baby_weight = tk.Label(tab_record_birth, text='Baby Weight')
entry_baby_weight = tk.Entry(tab_record_birth)
label_baby_length = tk.Label(tab_record_birth, text='Baby Length')
entry_baby_length = tk.Entry(tab_record_birth)
label_baby_gestational_age = tk.Label(tab_record_birth, text='Baby Gestational Age')
entry_baby_gestational_age = tk.Entry(tab_record_birth)
label_delivery_method = tk.Label(tab_record_birth, text='Delivery Method')
entry_delivery_method = tk.Entry(tab_record_birth)
label_complications = tk.Label(tab_record_birth, text='Complications')
entry_complications = tk.Entry(tab_record_birth)

# Position the labels and entry boxes in the Birth Record tab
label_patient_id.grid(row=0, column=0, padx=5, pady=5)
entry_patient_id.grid(row=0, column=1, padx=5, pady=5)
label_staff_id.grid(row=1, column=0, padx=5, pady=5)
entry_staff_id.grid(row=1, column=1, padx=5, pady=5)
label_birth_date_time.grid(row=2, column=0, padx=5, pady=5)
entry_birth_date_time.grid(row=2, column=1, padx=5, pady=5)
label_baby_first_name.grid(row=3, column=0, padx=5, pady=5)
entry_baby_first_name.grid(row=3, column=1, padx=5, pady=5)
label_baby_last_name.grid(row=4, column=0, padx=5, pady=5)
entry_baby_last_name.grid(row=4, column=1, padx=5, pady=5)
label_baby_weight.grid(row=5, column=0, padx=5, pady=5)
entry_baby_weight.grid(row=5, column=1, padx=5, pady=5)
label_baby_length.grid(row=6, column=0, padx=5, pady=5)
entry_baby_length.grid(row=6, column=1, padx=5, pady=5)
label_baby_gestational_age.grid(row=7, column=0, padx=5, pady=5)
entry_baby_gestational_age.grid(row=7, column=1, padx=5, pady=5)
label_delivery_method.grid(row=8, column=0, padx=5, pady=5)
entry_delivery_method.grid(row=8, column=1, padx=5, pady=5)
label_complications.grid(row=9, column=0, padx=5, pady=5)
entry_complications.grid(row=9, column=1, padx=5, pady=5)


# Create a function to record a birth
def record_birth():
    # Get the data from the entry boxes
    patient_id = entry_patient_id.get()
    staff_id = entry_staff_id.get()
    birth_date_time = entry_birth_date_time.get()
    baby_first_name = entry_baby_first_name.get()
    baby_last_name = entry_baby_last_name.get()
    baby_weight = entry_baby_weight.get()
    baby_length = entry_baby_length.get()
    baby_gestational_age = entry_baby_gestational_age.get()
    delivery_method = entry_delivery_method.get()
    complications = entry_complications.get()

    # Insert the data into the Birth_Record table
    sql = "INSERT INTO Birth_Record (patient_id, staff_id, birth_date_time, baby_first_name, baby_last_name, " \
          "baby_weight, baby_length, baby_gestational_age, delivery_method, complications) VALUES (%s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s)"
    val = (patient_id, staff_id, birth_date_time, baby_first_name, baby_last_name, baby_weight, baby_length,
           baby_gestational_age, delivery_method, complications)
    mycursor.execute(sql, val)
    mydb.commit()

    # Clear the entry boxes
    entry_patient_id.delete(0, 'end')
    entry_staff_id.delete(0, 'end')
    entry_birth_date_time.delete(0, 'end')
    entry_baby_first_name.delete(0, 'end')
    entry_baby_last_name.delete(0, 'end')
    entry_baby_weight.delete(0, 'end')
    entry_baby_length.delete(0, 'end')
    entry_baby_gestational_age.delete(0, 'end')
    entry_delivery_method.delete(0, 'end')
    entry_complications.delete(0, 'end')

    # Create a button to record a birth
button_record_birth = tk.Button(tab_record_birth, text="Record Birth", command=record_birth)
button_record_birth.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    # Pack the tab control and run the GUI
tab_control.pack(expand=1, fill='both')


root.mainloop()
