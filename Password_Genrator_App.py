import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Customize the style
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 16), foreground='blue', padding=(10, 10))  # Blue label text
        style.configure('TEntry', font=('Arial', 16), foreground='black', background='lightgray', padding=(10, 10), borderwidth=2, relief='solid')  # Black text on light gray entry box with border
        style.configure('TButton', font=('Arial', 16), foreground='green', background='blue', padding=(10, 10), borderwidth=2, relief='solid')  # Green text on blue button with border
        style.configure('TCombobox', font=('Arial', 16), foreground='black', background='lightgray', borderwidth=2, relief='solid')

        ttk.Label(self.master, text="Password Length:",foreground='black',).pack(pady=15)
        self.length_entry = ttk.Entry(self.master)
        self.length_entry.pack(pady=5)

        ttk.Label(self.master, text="Password Complexity:", font=('Arial', 16), foreground='black', padding=(10, 10)).pack(pady=15)
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")

        complexity_options = ["Low", "Medium", "High"]
        complexity_menu = ttk.Combobox(self.master, textvariable=self.complexity_var, values=complexity_options, style='TCombobox')
        complexity_menu.pack(pady=5)

        generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=15)

        self.generated_password_var = tk.StringVar()
        ttk.Entry(self.master, textvariable=self.generated_password_var, font=('Arial', 16, 'bold'), justify='center', state='readonly', foreground='blue', background='lightyellow').pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a valid positive length.")
                return

            characters = string.ascii_letters + string.digits

            generated_password = ''.join(random.choice(characters) for _ in range(length))
            self.generated_password_var.set(generated_password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
