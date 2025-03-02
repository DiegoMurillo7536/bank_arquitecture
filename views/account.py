import tkinter as tk
from tkinter import messagebox, ttk
from repositories.account import AccountRepository

class AccountUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Campo de entrada para el nombre de la cuenta
        tk.Label(self, text="Nombre de la cuenta:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_label = tk.Entry(self, width=30)
        self.entry_label.grid(row=0, column=1, padx=10, pady=10)

        # Checkbox para is_exempt
        self.is_exempt_var = tk.BooleanVar()
        self.is_exempt_check = tk.Checkbutton(self, text="Exento", variable=self.is_exempt_var)
        self.is_exempt_check.grid(row=1, column=0, padx=10, pady=10)

        # Input para account_type_id
        tk.Label(self, text="Tipo de cuenta:").grid(row=1, column=1, padx=10, pady=10)
        self.account_type_entry = tk.Entry(self, width=30)
        self.account_type_entry.grid(row=1, column=2, padx=10, pady=10)

        # Botón para agregar
        self.add_button = tk.Button(self, text="Agregar", command=self.add_account)
        self.add_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Lista de tipos de transacción
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10) 

        # Cargar tipos de transacción
        self.load_account()

    def add_account(self):      
        label = self.entry_label.get().strip()
        is_exempt = self.is_exempt_var.get()
        account_type_id = self.account_type_entry.get().strip()

        if not label:
            messagebox.showwarning("Advertencia", "El campo Nombre de la cuenta no puede estar vacío")
            return

        if not account_type_id:
            messagebox.showwarning("Advertencia", "Debe ingresar un tipo de cuenta")
            return

        AccountRepository.create(label, is_exempt, account_type_id)
        self.entry_label.delete(0, tk.END)
        self.is_exempt_var.set(False)
        self.account_type_entry.delete(0, tk.END)
        self.load_account()
        messagebox.showinfo("Éxito", f"'{label}' agregado correctamente.")

    def load_account(self):
        self.listbox.delete(0, tk.END)
        account = AccountRepository.get_all()
        for t in account:
            self.listbox.insert(tk.END, f"{t.id_account}: {t.label} - Exento: {t.is_exempt} - Tipo: {t.account_type_id}")