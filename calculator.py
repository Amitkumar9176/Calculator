import tkinter as tk

# Initialize the main application window
app = tk.Tk()
app.title("Calculator")

# Global variable to store the input expression
expression = ""

# Function to update the expression in the input field
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate the expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)  # Update the input field with the result
        expression = result  # Save the result for further calculations
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# StringVar to store the input text
input_text = tk.StringVar()

# Input field
input_field = tk.Entry(app, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Loop through buttons list to create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(app, text=text, padx=20, pady=20, command=equalpress)
    else:
        btn = tk.Button(app, text=text, padx=20, pady=20, command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(app, text='C', padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
app.mainloop()