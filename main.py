import tkinter
from tkinter import ttk

# Create the main window
conversion_window = tkinter.Tk()
conversion_window.title("Value Conversions")
conversion_window.resizable(1,1)

# Define the fonts and colors to be used
field_font = ("Arial", 12)
bg_color = "white"
button_color = "grey"
conversion_window.config(bg = bg_color)

# Define the function to perform the conversion
def convert():
    # Retrieve the input value and selected metric options
    input_value = float(input_field.get())
    input_metric = input_combobox.get()
    output_metric = output_combobox.get()

    # Define the conversion ratios
    ratios = {'millimeters': 1000, 'centimeters': 100, 'meters': 1, 'kilometers': 0.001}

    # Convert the input value to meters
    meters_value = input_value / ratios[input_metric]

    # Convert meters to the output metric
    output_value = meters_value * ratios[output_metric]

    # Update the output field with the converted value
    output_field.delete(0, tkinter.END)
    output_field.insert(0, str(output_value))

# Create the input and output fields
input_field = tkinter.Entry(conversion_window, width=20, font=field_font, borderwidth=3)
output_field = tkinter.Entry(conversion_window, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(conversion_window, text="=", font=field_font, bg=bg_color)

# Add the input and output fields to the window
input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

# Create a default value for the input field
input_field.insert(0, 'Enter your quantity')

# Create the metric options
metric_list = ['millimeters', 'centimeters', 'meters', 'kilometers']
input_combobox = ttk.Combobox(conversion_window, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(conversion_window, value=metric_list, font=field_font, justify='center')
to_label = tkinter.Label(conversion_window, text="to", font=field_font, bg=bg_color)

# Add the metric options to the window
input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

# Set default metric options
input_combobox.set('meters')
output_combobox.set('meters')

# Create the conversion button
convert_button = tkinter.Button(conversion_window, text='Convert', font=field_font, bg=button_color, command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

# Start the main event loop
conversion_window.mainloop()

import tkinter as tk
from tkinter import ttk

# Define the conversion factors
conversions = {
    "inch": 39.37,
    "foot": 3.28,
    "yard": 1.09,
    "mile": 0.00062
}

# Define the main function
def convert():
    try:
        value = float(entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()
        result = round(value * conversions[from_unit] / conversions[to_unit], 2)
        output.config(state="normal")
        output.delete(0, tk.END)
        output.insert(0, str(result))
        output.config(state="readonly")
    except ValueError:
        output.config(state="normal")
        output.delete(0, tk.END)
        output.insert(0, "Invalid input")
        output.config(state="readonly")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

# Create the input field
entry = tk.Entry(root)
entry.place(relx=0.25, rely=0.2, relwidth=0.5)

# Create the "from" combobox
from_combobox = ttk.Combobox(root, values=list(conversions.keys()))
from_combobox.current(0)
from_combobox.place(relx=0.1, rely=0.5, relwidth=0.3)

# Create the "to" combobox
to_combobox = ttk.Combobox(root, values=list(conversions.keys()))
to_combobox.current(1)
to_combobox.place(relx=0.6, rely=0.5, relwidth=0.3)

# Create the output field
output = tk.Entry(root, state="readonly")
output.place(relx=0.25, rely=0.8, relwidth=0.5)

# Create the convert button
button = tk.Button(root, text="Convert", command=convert)
button.place(relx=0.4, rely=0.4)

# Run the main loop
root.mainloop()

import tkinter as tk
from tkinter import ttk

# Define the conversion factors
conversions = {
    "inch": 39.37,
    "foot": 3.28,
    "yard": 1.09,
    "mile": 0.00062
}

# Define the main function
def convert():
    try:
        value = float(entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()
        result = round(value * conversions[from_unit] / conversions[to_unit], 2)
        output.config(state="normal")
        output.delete(0, tk.END)
        output.insert(0, str(result))
        output.config(state="readonly")
    except ValueError:
        output.config(state="normal")
        output.delete(0, tk.END)
        output.insert(0, "Invalid input")
        output.config(state="readonly")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x200")

# Create the input field
entry = tk.Entry(root)
entry.place(relx=0.25, rely=0.2, relwidth=0.5)

# Create the "from" combobox
from_combobox = ttk.Combobox(root, values=list(conversions.keys()))
from_combobox.current(0)
from_combobox.place(relx=0.1, rely=0.5, relwidth=0.3)

# Create the "to" combobox
to_combobox = ttk.Combobox(root, values=list(conversions.keys()))
to_combobox.current(1)
to_combobox.place(relx=0.6, rely=0.5, relwidth=0.3)

# Create the output field
output = tk.Entry(root, state="readonly")
output.place(relx=0.25, rely=0.8, relwidth=0.5)

# Create the convert button
button = tk.Button(root, text="Convert", command=convert)
button.place(relx=0.4, rely=0.4)

# Run the main loop
root.mainloop()


