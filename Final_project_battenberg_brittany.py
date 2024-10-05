# Final Project
# author: Brittany Battenberg
# created: 2024-13-10

""" This program will take input from a medical staff as a patient form."""

# importing in tkinter
import tkinter 
from tkinter import ttk

def load_frame2():
    print("Hello World")

# initialize app 
window = tkinter.Tk()
window.title("Patient Visit Report")

 # saving patient demographics
patient_info_frame = tkinter.LabelFrame(window, text="Patient Information", bg="light green")
patient_info_frame.grid(row=0, column=0, padx=20, pady=20)

# frame 1 widgets
first_name_label = tkinter.Label(patient_info_frame, text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(patient_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)
first_name_entry = tkinter.Entry(patient_info_frame)
last_name_entry = tkinter.Entry(patient_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)
gender_label = tkinter.Label(patient_info_frame, text="Gender")
gender_combobox = ttk.Combobox(patient_info_frame, values = ["", "Male", "Female", "Other","Prefer Not to Say",""])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)
date_of_birth_label = tkinter.Label(patient_info_frame, text="Date of Birth")
date_of_birth_label.grid(row=2, column=0)
date_of_birth_entry = tkinter.Entry(patient_info_frame)
date_of_birth_entry.grid(row=3,column=0)
address_label=tkinter.Label(patient_info_frame, text="Address")
address_label.grid(row=2,column=1)
address_entry=tkinter.Entry(patient_info_frame)
address_entry.grid(row=3, column=1)
phone_label=tkinter.Label(patient_info_frame, text="Phone")
phone_label.grid(row=2, column=2)
phone_entry=tkinter.Entry(patient_info_frame)
phone_entry.grid(row=3, column=2)

# button widget
next_button1=tkinter.Button(patient_info_frame, text="NEXT", font=("Arial", 20), cursor="hand2", command=load_frame2())
next_button1.pack(pady=20)

next_button1.config(command=lambda: load_frame2)


# run app
window.mainloop()
