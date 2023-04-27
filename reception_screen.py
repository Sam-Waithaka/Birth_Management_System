import tkinter as tk

class ReceptionScreen:
    def __init__(self, master):
        self.master = master
        master.title("Reception Screen")

        # Create the "Book Appointment" button
        self.book_appointment_button = tk.Button(master, text="Book Appointment", command=self.book_appointment)
        self.book_appointment_button.pack()

        # Create the "Register Patient" button
        self.register_patient_button = tk.Button(master, text="Register Patient", command=self.register_patient)
        self.register_patient_button.pack()

    def book_appointment(self):
        import appointments

    def register_patient(self):
        import registering_new_patients

root = tk.Tk()
reception_screen = ReceptionScreen(root)
root.mainloop()
