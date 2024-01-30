import tkinter as tk
from tkinter import ttk, messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = []
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.master, columns=('Name', 'Phone', 'Email', 'Address'), show='headings')
        self.tree.heading('Name', text='Name', anchor='center')
        self.tree.heading('Phone', text='Phone', anchor='center')
        self.tree.heading('Email', text='Email', anchor='center')
        self.tree.heading('Address', text='Address', anchor='center')
        self.tree.pack(padx=10, pady=10)
        self.tree.bind('<Double-1>', self.on_item_double_click)  # Bind double-click event

        add_button = ttk.Button(self.master, text="Add Contact", command=self.add_contact, style='TButton')
        add_button.pack(pady=10)

        update_button = ttk.Button(self.master, text="Update Contact", command=self.update_contact, style='TButton')
        update_button.pack(pady=10)

        delete_button = ttk.Button(self.master, text="Delete Contact", command=self.delete_contact, style='TButton')
        delete_button.pack(pady=10)

        refresh_button = ttk.Button(self.master, text="Refresh", command=self.refresh_contacts, style='TButton')
        refresh_button.pack(pady=10)

        search_label = ttk.Label(self.master, text="Search:", font=('Arial', 16), foreground='blue')
        search_label.pack()
        self.search_entry = ttk.Entry(self.master, font=('Arial', 14))
        self.search_entry.pack(pady=10)
        search_button = ttk.Button(self.master, text="Search", command=self.search_contact, style='TButton')
        search_button.pack(pady=10)

        # Customize the style for buttons and labels
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14), foreground='black', background='lightblue', padding=(10, 10))
        style.configure('TLabel', font=('Arial', 16), foreground='blue')

    def add_contact(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Contact")

        ttk.Label(add_window, text="Name:", font=('Arial', 16), foreground='blue', background='lightblue').pack(pady=5)
        name_entry = ttk.Entry(add_window, font=('Arial', 14))
        name_entry.pack(pady=5)

        ttk.Label(add_window, text="Phone:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        phone_entry = ttk.Entry(add_window, font=('Arial', 14))
        phone_entry.pack(pady=5)

        ttk.Label(add_window, text="Email:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        email_entry = ttk.Entry(add_window, font=('Arial', 14))
        email_entry.pack(pady=5)

        ttk.Label(add_window, text="Address:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        address_entry = ttk.Entry(add_window, font=('Arial', 14))
        address_entry.pack(pady=5)

        save_button = ttk.Button(add_window, text="Save", command=lambda: self.save_contact(
            name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), add_window), style='TButton')
        save_button.pack(pady=10)

    def save_contact(self, name, phone, email, address, add_window):
        if not name or not phone:
            messagebox.showerror("Error", "Name and phone are required.")
            return

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.update_contact_list()
        add_window.destroy()

    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a contact to update.")
            return

        # Extract the item identifier from the tuple
        selected_item_id = selected_item[0]

        # Convert the item identifier to integer index
        try:
            index = int(self.tree.index(selected_item_id))
        except ValueError:
            messagebox.showerror("Error", "Invalid selection.")
            return

        selected_contact = self.contacts[index]
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Contact")

        ttk.Label(update_window, text="Name:", font=('Arial', 16), foreground='blue', background='lightblue').pack(pady=5)
        name_entry = ttk.Entry(update_window, font=('Arial', 14))
        name_entry.insert(0, selected_contact.name)
        name_entry.pack(pady=5)

        ttk.Label(update_window, text="Phone:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        phone_entry = ttk.Entry(update_window, font=('Arial', 14))
        phone_entry.insert(0, selected_contact.phone)
        phone_entry.pack(pady=5)

        ttk.Label(update_window, text="Email:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        email_entry = ttk.Entry(update_window, font=('Arial', 14))
        email_entry.insert(0, selected_contact.email)
        email_entry.pack(pady=5)

        ttk.Label(update_window, text="Address:", font=('Arial', 16), foreground='black', background='lightblue').pack(pady=5)
        address_entry = ttk.Entry(update_window, font=('Arial', 14))
        address_entry.insert(0, selected_contact.address)
        address_entry.pack(pady=5)

        save_button = ttk.Button(update_window, text="Save", command=lambda: self.perform_update(
            index, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), update_window), style='TButton')
        save_button.pack(pady=10)

    def perform_update(self, index, name, phone, email, address, update_window):
        if not name or not phone:
            messagebox.showerror("Error", "Name and phone are required.")
            return

        contact = Contact(name, phone, email, address)
        self.contacts[index] = contact
        self.update_contact_list()
        update_window.destroy()

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a contact to delete.")
            return

        # Extract the item identifier from the tuple
        selected_item_id = selected_item[0]

        # Convert the item identifier to integer index
        try:
            index = int(self.tree.index(selected_item_id))
        except ValueError:
            messagebox.showerror("Error", "Invalid selection.")
            return

        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[index]
            self.tree.delete(selected_item)
            self.update_contact_list()

    def search_contact(self):
        keyword = self.search_entry.get().lower()
        if not keyword:
            self.update_contact_list()
            return

        matching_contacts = [contact for contact in self.contacts if
                             keyword in contact.name.lower() or keyword in contact.phone]
        self.display_contacts(matching_contacts)

    def refresh_contacts(self):
        self.update_contact_list()

    def on_item_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.update_contact()

    def update_contact_list(self):
        self.display_contacts(self.contacts)

    def display_contacts(self, contacts):
        self.tree.delete(*self.tree.get_children())
        for contact in contacts:
            self.tree.insert('', 'end', values=(contact.name, contact.phone, contact.email, contact.address))

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
