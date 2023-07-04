import tkinter as tk
from tkinter import ttk

user_inputs = []

def submit_pregnancies():
    pregnancies = entry_pregnancies.get()
    user_inputs.append(pregnancies)
    label_pregnancies.config(text="You entered Pregnancies: " + pregnancies)
    window_glucose.deiconify()
    window_pregnancies.withdraw()

def submit_glucose():
    glucose = entry_glucose.get()
    user_inputs.append(glucose)
    label_glucose.config(text="You entered Glucose: " + glucose)
    window_blood_pressure.deiconify()
    window_glucose.withdraw()

def submit_blood_pressure():
    blood_pressure = entry_blood_pressure.get()
    user_inputs.append(blood_pressure)
    label_blood_pressure.config(text="You entered Blood Pressure: " + blood_pressure)
    window_skin_thickness.deiconify()
    window_blood_pressure.withdraw()

def submit_skin_thickness():
    skin_thickness = entry_skin_thickness.get()
    user_inputs.append(skin_thickness)
    label_skin_thickness.config(text="You entered Skin Thickness: " + skin_thickness)
    window_insulin.deiconify()
    window_skin_thickness.withdraw()

def submit_insulin():
    insulin = entry_insulin.get()
    user_inputs.append(insulin)
    label_insulin.config(text="You entered Insulin: " + insulin)
    window_bmi.deiconify()
    window_insulin.withdraw()

def submit_bmi():
    bmi = entry_bmi.get()
    user_inputs.append(bmi)
    label_bmi.config(text="You entered BMI: " + bmi)
    window_diabetes_pedigree_function.deiconify()
    window_bmi.withdraw()

def submit_diabetes_pedigree_function():
    diabetes_pedigree_function = entry_diabetes_pedigree_function.get()
    user_inputs.append(diabetes_pedigree_function)
    label_diabetes_pedigree_function.config(text="You entered Diabetes Pedigree Function: " + diabetes_pedigree_function)
    window_age.deiconify()
    window_diabetes_pedigree_function.withdraw()

def submit_age():
    age = entry_age.get()
    user_inputs.append(age)
    label_age.config(text="You entered Age: " + age)
    window_age.withdraw()

# Window for Pregnancies
window_pregnancies = tk.Tk()
window_pregnancies.title("Pregnancies")
window_pregnancies.geometry("300x150")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

label_pregnancies = ttk.Label(window_pregnancies, text="Please enter the number of pregnancies:")
label_pregnancies.pack(pady=10)

entry_pregnancies = ttk.Entry(window_pregnancies, font=("Arial", 12))
entry_pregnancies.pack(pady=10)

button_pregnancies = ttk.Button(window_pregnancies, text="Submit", command=submit_pregnancies)
button_pregnancies.pack(pady=10)

# Window for Glucose
window_glucose = tk.Toplevel(window_pregnancies)
window_glucose.title("Glucose")
window_glucose.geometry("300x150")
window_glucose.withdraw()

label_glucose = ttk.Label(window_glucose, text="Please enter the glucose level:")
label_glucose.pack(pady=10)

entry_glucose = ttk.Entry(window_glucose, font=("Arial", 12))
entry_glucose.pack(pady=10)

button_glucose = ttk.Button(window_glucose, text="Submit", command=submit_glucose)
button_glucose.pack(pady=10)

# Window for Blood Pressure
window_blood_pressure = tk.Toplevel(window_glucose)
window_blood_pressure.title("Blood Pressure")
window_blood_pressure.geometry("300x150")
window_blood_pressure.withdraw()

label_blood_pressure = ttk.Label(window_blood_pressure, text="Please enter the blood pressure:")
label_blood_pressure.pack(pady=10)

entry_blood_pressure = ttk.Entry(window_blood_pressure, font=("Arial", 12))
entry_blood_pressure.pack(pady=10)

button_blood_pressure = ttk.Button(window_blood_pressure, text="Submit", command=submit_blood_pressure)
button_blood_pressure.pack(pady=10)

# Window for Skin Thickness
window_skin_thickness = tk.Toplevel(window_blood_pressure)
window_skin_thickness.title("Skin Thickness")
window_skin_thickness.geometry("300x150")
window_skin_thickness.withdraw()

label_skin_thickness = ttk.Label(window_skin_thickness, text="Please enter the skin thickness:")
label_skin_thickness.pack(pady=10)

entry_skin_thickness = ttk.Entry(window_skin_thickness, font=("Arial", 12))
entry_skin_thickness.pack(pady=10)

button_skin_thickness = ttk.Button(window_skin_thickness, text="Submit", command=submit_skin_thickness)
button_skin_thickness.pack(pady=10)

# Window for Insulin
window_insulin = tk.Toplevel(window_skin_thickness)
window_insulin.title("Insulin")
window_insulin.geometry("300x150")
window_insulin.withdraw()

label_insulin = ttk.Label(window_insulin, text="Please enter the insulin level:")
label_insulin.pack(pady=10)

entry_insulin = ttk.Entry(window_insulin, font=("Arial", 12))
entry_insulin.pack(pady=10)

button_insulin = ttk.Button(window_insulin, text="Submit", command=submit_insulin)
button_insulin.pack(pady=10)

# Window for BMI
window_bmi = tk.Toplevel(window_insulin)
window_bmi.title("BMI")
window_bmi.geometry("300x150")
window_bmi.withdraw()

label_bmi = ttk.Label(window_bmi, text="Please enter the BMI (Body Mass Index):")
label_bmi.pack(pady=10)

entry_bmi = ttk.Entry(window_bmi, font=("Arial", 12))
entry_bmi.pack(pady=10)

button_bmi = ttk.Button(window_bmi, text="Submit", command=submit_bmi)
button_bmi.pack(pady=10)

# Window for Diabetes Pedigree Function
window_diabetes_pedigree_function = tk.Toplevel(window_bmi)
window_diabetes_pedigree_function.title("Diabetes Pedigree Function")
window_diabetes_pedigree_function.geometry("300x150")
window_diabetes_pedigree_function.withdraw()

label_diabetes_pedigree_function = ttk.Label(window_diabetes_pedigree_function, text="Please enter the diabetes pedigree function:")
label_diabetes_pedigree_function.pack(pady=10)

entry_diabetes_pedigree_function = ttk.Entry(window_diabetes_pedigree_function, font=("Arial", 12))
entry_diabetes_pedigree_function.pack(pady=10)

button_diabetes_pedigree_function = ttk.Button(window_diabetes_pedigree_function, text="Submit", command=submit_diabetes_pedigree_function)
button_diabetes_pedigree_function.pack(pady=10)

# Window for Age
window_age = tk.Toplevel(window_diabetes_pedigree_function)
window_age.title("Age")
window_age.geometry("300x150")
window_age.withdraw()

label_age = ttk.Label(window_age, text="Please enter your age:")
label_age.pack(pady=10)

entry_age = ttk.Entry(window_age, font=("Arial", 12))
entry_age.pack(pady=10)

button_age = ttk.Button(window_age, text="Submit", command=submit_age)
button_age.pack(pady=10)

# Test input-saving
print(user_inputs)

window_pregnancies.mainloop()


# Test input-saving
print(user_inputs)
