import tkinter as tk
from tkinter import ttk

def calculate_tax():
    try:
        income = float(income_entry.get())
        tax_percent = float(tax_percent_entry.get())

        tax_amount = (tax_percent / 100) * income
        net_income = income - tax_amount

        result_label.config(text=f"Net Income after Tax: ₹{net_income:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Tax Calculator (INR)")

# Create and place widgets
income_label = ttk.Label(root, text="Income:")
income_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

income_entry = ttk.Entry(root)
income_entry.grid(row=0, column=1, padx=10, pady=10)

tax_percent_label = ttk.Label(root, text="Tax Percentage:")
tax_percent_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

tax_percent_entry = ttk.Entry(root)
tax_percent_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
