import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta


def calculate_age():
    try:
        birth_date = input_entry.get_date()
        today = datetime.now().date()
        age = relativedelta(today, birth_date)

        years_str = f"{age.years} {'year' if age.years == 1 else 'years'}"
        months_str = f"{age.months} {'month' if age.months == 1 else 'months'}"
        days_str = f"{age.days} {'day' if age.days == 1 else 'days'}"

        result_label.config(text=f"Age: {years_str}, {months_str}, {days_str}")
    except ValueError:
        messagebox.showerror("Error", "Choose correct date of birth.")


window = tk.Tk()
window.title("Age calculator")
window.geometry('400x300')

frame = tk.Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

input_label = tk.Label(
    frame,
    text="Date of birth (dd/mm/yy):"
)
input_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")

input_entry = DateEntry(
    frame,
    width=12,
    background='darkblue',
    foreground='white',
    date_pattern='dd/mm/y',
    borderwidth=2
)
input_entry.grid(row=0, column=1)

calculate_btn = tk.Button(
    frame,
    text="Calculate",
    command=calculate_age
)
calculate_btn.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(
    frame,
    text=""
)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
