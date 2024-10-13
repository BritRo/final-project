# Final Project
# author: Brittany Battenberg
# created: 2024-13-10

""" This program will take input from a medical staff as a patient form. It will save patient information to be used at another time."""

import tkinter
from tkinter import ttk 
from PIL import Image, ImageTk
import tkinter.messagebox as box


def save_frame1():
    # User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    gender = gender_combobox.get()
    dateofbirth = date_of_birth_entry.get()
    address = address_entry.get()
    phone = address_entry.get()

    # insurance info
    insurancename = insurance_name_entry.get()
    insurancepolicy =insurance_policy_entry.get()
    insurancepolicyid = insurance_id_num_entry.get()
    insurancemailingaddress = insurance_mailing_add_entry.get()
   

    print("Full Name: ", firstname + " ", lastname, "Gender:", gender, "Date of Birth:", dateofbirth)
    print("Address: ", address, "Phone Number: ", phone)
    print("----------------------------")
    print("Insurance: ", insurancename, "Policy #: ", insurancepolicy, "Payor ID #: ", insurancepolicyid, "Insurance Mailing Address: " \
          ,insurancemailingaddress)
    


def load_frame2():
    new_window = tkinter.Toplevel(window, bg="light sea green")
    new_window.title("Vital Signs")
    new_window.geometry("900x900")

    # first frame on new window
    vital_info_frame=tkinter.LabelFrame(new_window, text="Patient Visit and Vitals", bg="light sea green")
    vital_info_frame.grid(row=0, column=0, sticky="news", padx=40, pady=10)

    # widgets for first frame on new window
    visit_reason_label = tkinter.Label(vital_info_frame, text="Reason for Visit",bg="light sea green")
    visit_reason_combobox = ttk.Combobox(vital_info_frame, values = ["", "Annual Exam", "Sick Visit", "Vaccination","Other"])
    visit_reason_label.grid(row=0, column=1)
    visit_reason_combobox.grid(row=1, column=1)
    height_label=tkinter.Label(vital_info_frame, text="Height(inches)",bg="light sea green")
    height_label_entry=tkinter.Entry(vital_info_frame)
    height_label.grid(row=0, column=2)
    height_label_entry.grid(row=1, column=2)
    weight_label=tkinter.Label(vital_info_frame, text="Weight(lbs)", bg="light sea green")
    weight_label_entry=tkinter.Entry(vital_info_frame)
    weight_label.grid(row=0, column=3)
    weight_label_entry.grid(row=1, column=3)
    temp_label=tkinter.Label(vital_info_frame, text="Temperature", bg="light sea green")
    temp_label_entry=tkinter.Entry(vital_info_frame)
    temp_label.grid(row=0, column=4)
    temp_label_entry.grid(row=1, column=4)
    temp_location_label=tkinter.Label(vital_info_frame, text="Temp Location", bg="light sea green")
    temp_location_combobox=ttk.Combobox(vital_info_frame, values=["", "Oral", "Ear", "Forehead","Armpit", "Rectal"])
    temp_location_label.grid(row=0, column=5)
    temp_location_combobox.grid(row=1, column=5)
    pulse_ox_label=tkinter.Label(vital_info_frame, text="Pulse Ox", bg="light sea green")
    pulse_ox_label_entry=tkinter.Entry(vital_info_frame)
    pulse_ox_label.grid(row=2, column=1)
    pulse_ox_label_entry.grid(row=3, column=1)
    blood_press_label=tkinter.Label(vital_info_frame, text="Blood Pressure", bg="light sea green")
    blood_press_label_entry=tkinter.Entry(vital_info_frame)
    blood_press_label.grid(row=2, column=2)
    blood_press_label_entry.grid(row=3, column=2)

    # Second Frame on new window
    physician_entry_frame=tkinter.LabelFrame(new_window, text="Physician System Review", bg="light sea green")
    physician_entry_frame.grid(row=6, column=0, sticky="news", padx=40, pady=10)

    # defining variables for checkboxes
    var3=tkinter.IntVar()
    var4=tkinter.IntVar()
    var5=tkinter.IntVar()
    var6=tkinter.IntVar()
    var7=tkinter.IntVar()
    var8=tkinter.IntVar()
    var9=tkinter.IntVar()
    var10=tkinter.IntVar()

    # build checkbox
    c3=tkinter.Checkbutton(physician_entry_frame, text="Neurological",bg="light sea green", variable=var3)
    c3.grid(row=7, column=1)
    c4=tkinter.Checkbutton(physician_entry_frame, text="Cardiovascular", bg="light sea green", variable=var4)
    c4.grid(row=7, column=2)
    c5=tkinter.Checkbutton(physician_entry_frame, text="Respiratory", bg="light sea green", variable=var5)
    c5.grid(row=7, column=3)
    c6=tkinter.Checkbutton(physician_entry_frame,text="Gastrointestinal", bg="light sea green", variable=var6)
    c6.grid(row=7, column=4)
    c7=tkinter.Checkbutton(physician_entry_frame, text="Genitourinary", bg="light sea green",variable=var7)
    c7.grid(row=7, column=5)
    c8=tkinter.Checkbutton(physician_entry_frame, text="Musculoskeletal", bg="light sea green", variable=var8)
    c8.grid(row=7, column=6)
    c9=tkinter.Checkbutton(physician_entry_frame, text="Integumentary", bg="light sea green", variable=var9)
    c9.grid(row=7, column=7)
    c10=tkinter.Checkbutton(physician_entry_frame, text="Psychosocial", bg="light sea green", variable=var10)
    c10.grid(row=7, column=8)

    # Physician Abnormal Finding Free Form Box 
    physician_notes=tkinter.Label(physician_entry_frame, text="Abnormal System Findings Notes: ", bg="light sea green")
    physician_notes.grid(row=8, column=1)
    physician_notes_entry=tkinter.Entry(physician_entry_frame)
    physician_notes_entry.grid(row=9, column=1)

    # third frame on new window
    follow_up_notes_frame=tkinter.LabelFrame(new_window, text="Visit Outcome", bg="light sea green")
    follow_up_notes_frame.grid(row=10, column=0, sticky="news", padx=40, pady=10)

    # third frame widgets
    vac_site_label=tkinter.Label(follow_up_notes_frame, text="Vaccination Site", bg="light sea green")
    vac_site_label.grid(row=11, column=1)
    vac_site_combobox=ttk.Combobox(follow_up_notes_frame, values=["Upper Arm", "Upper Thigh"])
    vac_site_combobox.grid(row=12, column=1)
    vac_num_label=tkinter.Label(follow_up_notes_frame, text="Vaccination Lot #:", bg="light sea green")
    vac_num_label.grid(row=11, column=2)
    vac_num_entry=tkinter.Entry(follow_up_notes_frame)
    vac_num_entry.grid(row=12, column=2)
    staff_follow_label=tkinter.Label(follow_up_notes_frame, text="Patient Follow Up", bg="light sea green")
    staff_follow_label.grid(row=13, column=1)

    # check box follow up 
    var11=tkinter.IntVar()
    var12=tkinter.IntVar()
    var13=tkinter.IntVar()
    var14=tkinter.IntVar()

    # create check button widget
    opt1=tkinter.Checkbutton(follow_up_notes_frame, text="STAT Labs", bg="light sea green", variable=var11)
    opt1.grid(row=14, column=1)
    opt2=tkinter.Checkbutton(follow_up_notes_frame, text="Radiology", bg="light sea green", variable=var12)
    opt2.grid(row=14, column=2)
    opt3=tkinter.Checkbutton(follow_up_notes_frame, text="Auth Request", bg="light sea green", variable=var13)
    opt3.grid(row=14, column=3)
    opt4=tkinter.Checkbutton(follow_up_notes_frame, text="Schedule Follow Up Appt", bg="light sea green", variable=var14)
    opt4.grid(row=14, column=4)

    # function to display options in checkbox
    def dialog2():
        c = "You Selected:"
        if var11.get()== 1: c += '\nSTAT Labs'
        if var12.get()== 1: c += '\nRadiology'
        if var13.get()== 1: c += '\nAuth Request'
        if var14.get()== 1: c += "\nSchedule Follow Up Appt"
        box.showinfo('Selection', c)

    # button to call the function 
    btn2=tkinter.Button(follow_up_notes_frame, text="Select", command=dialog2)
    btn2.grid(row=14, column=5)

    # image frame
    image_frame=tkinter.LabelFrame(new_window)
    image_frame.grid(row=16, column=0)
    
    # load the image using Pillow
    image_path="C:\\Python Files\\Sev140\\med image 1.png"
    # replace with your image path
    image=Image.open(image_path)
    photo=ImageTk.PhotoImage(image)

    # create a label to display the image
    image_label=tkinter.Label(image_frame, image=photo)
    image_label.pack()


    # close the window
    close_btn=tkinter.Button(new_window, text="Close", font=("Arial", 20), cursor="hand2", command=quit)
    close_btn.grid(row=17, column=0)
   

# initialize app 
window = tkinter.Tk()
window.title("Patient Visit Report")
# Load the image
image = Image.open("C:\\Python Files\\Sev140\\diagnostic.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image as background
label = tkinter.Label(window, image=photo)
label.place(x=0, y=0)

 # Frame 1 on root (Patient Information Section)
patient_info_frame = tkinter.LabelFrame(window, text="Patient Information", bg="light sea green")
patient_info_frame.grid(row=0, column=0, sticky="news", padx=40, pady=10)

# frame 1 on root window widgets
first_name_label = tkinter.Label(patient_info_frame, text="First Name", bg="light sea green")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(patient_info_frame, text="Last Name",bg="light sea green")
last_name_label.grid(row=0,column=1)
first_name_entry = tkinter.Entry(patient_info_frame)
last_name_entry = tkinter.Entry(patient_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)
gender_label = tkinter.Label(patient_info_frame, text="Gender",bg="light sea green")
gender_combobox = ttk.Combobox(patient_info_frame, values = ["", "Male", "Female", "Other","Prefer Not to Say",""])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)
date_of_birth_label = tkinter.Label(patient_info_frame, text="Date of Birth",bg="light sea green")
date_of_birth_label.grid(row=2, column=0)
date_of_birth_entry = tkinter.Entry(patient_info_frame)
date_of_birth_entry.grid(row=3,column=0)
address_label=tkinter.Label(patient_info_frame, text="Address",bg="light sea green")
address_label.grid(row=2,column=1)
address_entry=tkinter.Entry(patient_info_frame)
address_entry.grid(row=3, column=1)
phone_label=tkinter.Label(patient_info_frame, text="Phone",bg="light sea green")
phone_label.grid(row=2, column=2)
phone_entry=tkinter.Entry(patient_info_frame)
phone_entry.grid(row=3, column=2)

# frame 2 on root (Insurance Section)
insurance_info_frame = tkinter.LabelFrame(window, text="Insurance Information", bg="light sea green")
insurance_info_frame.grid(row=4, column=0, sticky="news", padx=40, pady=10)

# insurance information section on root window
""" construct integer variable objects to store value"""
var1 = tkinter.BooleanVar()
var2 = tkinter.BooleanVar()

# create check button widget
insurance1 = tkinter.Checkbutton(insurance_info_frame, bg="light sea green", text="Insurance", \
                                 variable= var1)
insurance2 = tkinter.Checkbutton(insurance_info_frame,bg="light sea green", text="Private Pay", \
                                 variable=var2)
 
# function to display a check button 
def dialog():
    s = "Your Choice:"
    if var1.get() == 1 : s += '\n Medical Insurance'
    if var2.get() == 1 : s += '\n Private Pay'
    box.showinfo('Selection', s)

# button to call the function when clicked
btn = tkinter.Button(insurance_info_frame, text="Choose", command=dialog)

# add push button and check buttons to the frame
btn.grid(row=7, column=2)
insurance1.grid(row=7, column=0)
insurance2.grid(row=7, column=1)

insurance_name=tkinter.Label(insurance_info_frame, text="Insurance Name", bg="light sea green")
insurance_name.grid(row=8, column=0)
insurance_name_entry=tkinter.Entry(insurance_info_frame)
insurance_name_entry.grid(row=9, column=0)
insurance_policy=tkinter.Label(insurance_info_frame, text="Policy Number",bg="light sea green")
insurance_policy.grid(row=8, column=1)
insurance_policy_entry=tkinter.Entry(insurance_info_frame)
insurance_policy_entry.grid(row=9, column=1)
insurance_id_num=tkinter.Label(insurance_info_frame, text="Policy ID Number", bg="light sea green")
insurance_id_num.grid(row=8,column=2)
insurance_id_num_entry=tkinter.Entry(insurance_info_frame)
insurance_id_num_entry.grid(row=9, column=2)
insurance_mailing_add=tkinter.Label(insurance_info_frame, text="Mailing Address", bg="light sea green")
insurance_mailing_add.grid(row=10, column=0)
insurance_mailing_add_entry=tkinter.Entry(insurance_info_frame)
insurance_mailing_add_entry.grid(row=11, column=0)


# button for to save information and to move to the next screen
button1 = tkinter.Button(window, text="Save", font=("Arial", 20), cursor="hand2",command=save_frame1)
button1.grid(row=13, column=0, sticky= "news")
button2 = tkinter.Button(window, text="Next", font=("Arial", 20), cursor="hand2", command=load_frame2)
button2.grid(row=13, column=1, sticky="news")

# run app
window.mainloop() 