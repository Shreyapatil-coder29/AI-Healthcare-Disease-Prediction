import tkinter as tk
import numpy as np
from tkinter import messagebox

# Function to check disease risk
def check_disease():
    try:
        glucose = float(glucose_entry.get())
        bp = float(bp_entry.get())
        bmi = float(bmi_entry.get())
        age = int(age_entry.get())

        patient = np.array([glucose, bp, bmi, age])
        threshold = np.array([140, 90, 25, 45])

        risk = patient > threshold
        risk_score = np.sum(risk)

        if risk_score == 0:
            result = "Healthy"
        elif risk_score <= 2:
            result = "Moderate Risk"
        else:
            result = "High Risk of Diabetes"

        result_label.config(
            text=f"Risk Score: {risk_score}\nPrediction: {result}",
            fg="blue"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create window
root = tk.Tk()
root.title("Healthcare Disease Checkup")
root.geometry("400x400")

tk.Label(root, text="Healthcare Disease Checkup",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Glucose Level").pack()
glucose_entry = tk.Entry(root)
glucose_entry.pack()

tk.Label(root, text="Blood Pressure").pack()
bp_entry = tk.Entry(root)
bp_entry.pack()

tk.Label(root, text="BMI").pack()
bmi_entry = tk.Entry(root)
bmi_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root,
          text="Check Disease",
          command=check_disease,
          bg="green",
          fg="white").pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()