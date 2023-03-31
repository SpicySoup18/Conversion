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
