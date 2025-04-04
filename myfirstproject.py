import tkinter as tk
from tkinter import messagebox
import json
import os

# This function loads saved user data from a file
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return {}

# This function saves user data to a file
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to register a new user
def register_user():
    username = entry_user.get()  # Get the username from input box
    password = entry_password.get()  # Get the password from input box
    if username and password:
        data = load_data()  # Load the existing data
        if username in data:
            messagebox.showerror("Error", "User already exists!")
        else:
            data[username] = {"password": password, "info": {}}  # Add new user
            save_data(data)  # Save updated data
            messagebox.showinfo("Success", "User Registered!")
    else:
        messagebox.showerror("Error", "Please enter username and password!")

# Function to log in a user
def login_user():
    username = entry_user.get()  # Get the username from input box
    password = entry_password.get()  # Get the password from input box
    data = load_data()  # Load the existing data
    if username in data and data[username]["password"] == password:
        messagebox.showinfo("Success", "Login Successful!")
        open_dashboard(username)  # Open the dashboard after login
    else:
        messagebox.showerror("Error", "Invalid Credentials!")

# Function to open the user dashboard
def open_dashboard(username):
    login_window.destroy()  # Close the login window
    dashboard_window = tk.Tk()  # Create a new window for the dashboard
    dashboard_window.title("Dashboard")
    dashboard_window.configure(bg="#FF69B4")  # Set a background color

    # Display a welcome message
    tk.Label(dashboard_window, text="Hi, I'm glad to have you again!", font=("Arial", 18), bg="#FF69B4").pack(pady=10)

    # Buttons to access different features
    tk.Button(dashboard_window, text="Add Bank Details", command=lambda: add_bank_details(username), font=("Arial", 12)).pack(pady=10)
    tk.Button(dashboard_window, text="Add Extra Information", command=lambda: add_extra_info(username), font=("Arial", 12)).pack(pady=10)
    tk.Button(dashboard_window, text="Add Emergency Info", command=lambda: add_emergency_info(username), font=("Arial", 12)).pack(pady=10)
    tk.Button(dashboard_window, text="Add Notes", command=lambda: add_notes(username), font=("Arial", 12)).pack(pady=10)
    tk.Button(dashboard_window, text="Add User Data", command=lambda: add_user_data(username), font=("Arial", 12)).pack(pady=10)

    # Button to log out
    tk.Button(dashboard_window, text="Logout", command=dashboard_window.destroy, font=("Arial", 12)).pack(pady=10)

    dashboard_window.mainloop()  # Start the dashboard window

# Function to add bank details
def add_bank_details(username):
    bank_window = tk.Toplevel()
    bank_window.title("Add Bank Details")

    tk.Label(bank_window, text="Card Number:").pack()
    entry_card_number = tk.Entry(bank_window)
    entry_card_number.pack()

    tk.Label(bank_window, text="Expiry Date:").pack()
    entry_expiry_date = tk.Entry(bank_window)
    entry_expiry_date.pack()

    tk.Label(bank_window, text="Card CVV:").pack()
    entry_cvv = tk.Entry(bank_window)
    entry_cvv.pack()

    tk.Label(bank_window, text="Card Owner Name:").pack()
    entry_owner_name = tk.Entry(bank_window)
    entry_owner_name.pack()

    def save_bank_details():
        data = load_data()
        bank_details = {
            "card_number": entry_card_number.get(),
            "expiry_date": entry_expiry_date.get(),
            "cvv": entry_cvv.get(),
            "owner_name": entry_owner_name.get()
        }
        data[username]["info"]["bank_details"] = bank_details
        save_data(data)
        messagebox.showinfo("Success", "Bank Details Saved!")
        bank_window.destroy()

    tk.Button(bank_window, text="Save", command=save_bank_details).pack()

# Function to add extra information
def add_extra_info(username):
    extra_info_window = tk.Toplevel()
    extra_info_window.title("Add Extra Information")

    tk.Label(extra_info_window, text="Passport Details:").pack()
    entry_passport = tk.Entry(extra_info_window)
    entry_passport.pack()

    tk.Label(extra_info_window, text="Home Address:").pack()
    entry_home_address = tk.Entry(extra_info_window)
    entry_home_address.pack()

    tk.Label(extra_info_window, text="Blood Group:").pack()
    entry_blood_group = tk.Entry(extra_info_window)
    entry_blood_group.pack()

    tk.Label(extra_info_window, text="Permanent Address:").pack()
    entry_permanent_address = tk.Entry(extra_info_window)
    entry_permanent_address.pack()

    def save_extra_info():
        data = load_data()
        extra_info = {
            "passport_details": entry_passport.get(),
            "home_address": entry_home_address.get(),
            "blood_group": entry_blood_group.get(),
            "permanent_address": entry_permanent_address.get()
        }
        data[username]["info"]["extra_info"] = extra_info
        save_data(data)
        messagebox.showinfo("Success", "Extra Information Saved!")
        extra_info_window.destroy()

    tk.Button(extra_info_window, text="Save", command=save_extra_info).pack()

# Function to add emergency information
def add_emergency_info(username):
    emergency_window = tk.Toplevel()
    emergency_window.title("Add Emergency Information")

    tk.Label(emergency_window, text="Trustable Person Name:").pack()
    entry_trustable_name = tk.Entry(emergency_window)
    entry_trustable_name.pack()

    tk.Label(emergency_window, text="Trustable Person Contact:").pack()
    entry_trustable_contact = tk.Entry(emergency_window)
    entry_trustable_contact.pack()

    tk.Label(emergency_window, text="Present Address:").pack()
    entry_present_address = tk.Entry(emergency_window)
    entry_present_address.pack()

    tk.Label(emergency_window, text="Family Name:").pack()
    entry_family_name = tk.Entry(emergency_window)
    entry_family_name.pack()

    def save_emergency_info():
        data = load_data()
        emergency_info = {
            "trustable_name": entry_trustable_name.get(),
            "trustable_contact": entry_trustable_contact.get(),
            "present_address": entry_present_address.get(),
            "family_name": entry_family_name.get()
        }
        data[username]["info"]["emergency_info"] = emergency_info
        save_data(data)
        messagebox.showinfo("Success", "Emergency Information Saved!")
        emergency_window.destroy()

    tk.Button(emergency_window, text="Save", command=save_emergency_info).pack()

# Function to add notes
def add_notes(username):
    notes_window = tk.Toplevel()
    notes_window.title("Add Notes")

    tk.Label(notes_window, text="Day Routine:").pack()
    entry_day_routine = tk.Entry(notes_window)
    entry_day_routine.pack()

    tk.Label(notes_window, text="Next Planning:").pack()
    entry_next_planning = tk.Entry(notes_window)
    entry_next_planning.pack()

    tk.Label(notes_window, text="Occasion Timing:").pack()
    entry_occasion_timing = tk.Entry(notes_window)
    entry_occasion_timing.pack()

    tk.Label(notes_window, text="Exam Timing:").pack()
    entry_exam_timing = tk.Entry(notes_window)
    entry_exam_timing.pack()

    def save_notes():
        data = load_data()
        notes = {
            "day_routine": entry_day_routine.get(),
            "next_planning": entry_next_planning.get(),
            "occasion_timing": entry_occasion_timing.get(),
            "exam_timing": entry_exam_timing.get()
        }
        data[username]["info"]["notes"] = notes
        save_data(data)
        messagebox.showinfo("Success", "Notes Saved!")
        notes_window.destroy()

    tk.Button(notes_window, text="Save", command=save_notes).pack()

# Function to add user data
def add_user_data(username):
    user_data_window = tk.Toplevel()
    user_data_window.title("Add User Data")

    tk.Label(user_data_window, text="Social Accounts:").pack()
    entry_social_accounts = tk.Entry(user_data_window)
    entry_social_accounts.pack()

    tk.Label(user_data_window, text="Apple/Google ID:").pack()
    entry_apple_google_id = tk.Entry(user_data_window)
    entry_apple_google_id.pack()

    tk.Label(user_data_window, text="Gmail:").pack()
    entry_gmail = tk.Entry(user_data_window)
    entry_gmail.pack()

    def save_user_data():
        data = load_data()
        user_data = {
            "social_accounts": entry_social_accounts.get(),
            "apple_google_id": entry_apple_google_id.get(),
            "gmail": entry_gmail.get()
        }
        data[username]["info"]["user_data"] = user_data
        save_data(data)
        messagebox.showinfo("Success", "User Data Saved!")
        user_data_window.destroy()

    tk.Button(user_data_window, text="Save", command=save_user_data).pack()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Add a title to the login window
tk.Label(login_window, text="OPOP - Personal Info Storage", font=("Arial", 24), bg="#FFD700").pack(pady=50)

# Add a welcome message
tk.Label(login_window, text="Hi, I'm glad to have you again!", font=("Arial", 18), bg="#FFD700").pack(pady=20)

# Add input fields for username and password
tk.Label(login_window, text="Username:").pack()
entry_user = tk.Entry(login_window)
entry_user.pack(pady=5)

tk.Label(login_window, text="Password:").pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

# Add login and register buttons
tk.Button(login_window, text="Login", command=login_user, font=("Arial", 14)).pack(pady=10)
tk.Button(login_window, text="Register", command=register_user, font=("Arial", 14)).pack(pady=10)

login_window.mainloop()  # Start the login window