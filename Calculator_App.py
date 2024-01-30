import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    
    if button_value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == "AC":
        entry.delete(0, tk.END)
    elif button_value == "DEL":
        entry.delete(len(current_text) - 1, tk.END)
    elif button_value == "%":
        entry.insert(tk.END, "*0.01")
    else:
        entry.insert(tk.END, button_value)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x600")  # Increased height

# Entry widget for displaying the current expression
entry = tk.Entry(root, width=20, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Adjusted columnspan and added padding

# Define button colors
button_color = "#3498db"  # Blue color
text_color = "black"

# Button layout (rows and columns)
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('AC', 5, 0), ('DEL', 5, 1), ('%', 5, 2), ('()', 5, 3),
]

# Create buttons and assign colors
for (text, row, col) in button_layout:
    button = tk.Button(root, text=text, width=10, height=3, font=('Arial', 16),
                       bg=button_color, fg=text_color, command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=10, pady=10)

# Run the main loop
root.mainloop()
