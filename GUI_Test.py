import tkinter as tk
from tkinter import ttk

def submit_pregnancies():
    pregnancies = entry.get()
    label.config(text="You entered: " + pregnancies)

def submit_glucose():
    glucose = entry.get()
    label.config(text="You entered: " + glucose)

def submit_blood_pressure():
    blood_pressure = entry.get()
    label.config(text="You entered: " + blood_pressure)

def submit_skin_thickness():
    skin_thickness = entry.get()
    label.config(text="You entered: " + skin_thickness)

def submit_insulin():
    Insulin = entry.get()
    label.config(text="You entered: " + Insulin)

def submit_bmi():
    bmi = entry.get()
    label.config(text="You entered: " + bmi)

def submit_diabetes_pedigree():
    diabetes_pedigree = entry.get()
    label.config(text="You entered: " + diabetes_pedigree)

window = tk.Tk()
window.title("Pregnancy Tracker")
window.geometry("300x150")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

label = ttk.Label(window, text="Please enter the number of pregnancies:")
label.pack(pady=10)

entry = ttk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

button = ttk.Button(window, text="Submit", command=submit)
button.pack(pady=10)

window.mainloop()
