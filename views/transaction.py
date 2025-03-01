import tkinter as tk
from tkinter import messagebox
from repositories.transaction import TransactionRepository

class TransactionUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Campos de entrada
        tk.Label(self, text="Monto:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_amount = tk.Entry(self, width=30)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Descripción:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_description = tk.Entry(self, width=30)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self, text="ID Cuenta Origen:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_from_account = tk.Entry(self, width=30)
        self.entry_from_account.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self, text="ID Cuenta Destino:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_to_account = tk.Entry(self, width=30)
        self.entry_to_account.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self, text="ID Tipo de Transacción:").grid(row=4, column=0, padx=10, pady=10)
        self.entry_transaction_type = tk.Entry(self, width=30)
        self.entry_transaction_type.grid(row=4, column=1, padx=10, pady=10)

        # Botón para agregar transacción
        self.add_button = tk.Button(self, text="Agregar Transacción", command=self.add_transaction)
        self.add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Lista de transacciones
        self.listbox = tk.Listbox(self, width=80, height=10)
        self.listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
        
        # Cargar transacciones
        self.load_transactions()

    def add_transaction(self):
        try:
            amount = float(self.entry_amount.get().strip())
            description = self.entry_description.get().strip()
            id_from_account = int(self.entry_from_account.get().strip())
            id_to_account = int(self.entry_to_account.get().strip())
            id_transaction_type = int(self.entry_transaction_type.get().strip())

            if not description:
                messagebox.showwarning("Advertencia", "La descripción no puede estar vacía")
                return
            
            TransactionRepository.create(amount, description, id_from_account, id_to_account, id_transaction_type)
            self.clear_entries()
            self.load_transactions()
            messagebox.showinfo("Éxito", "Transacción agregada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos para los campos correspondientes.")

    def load_transactions(self):
        self.listbox.delete(0, tk.END)
        transactions = TransactionRepository.get_all()
        for t in transactions:
            self.listbox.insert(tk.END, f"ID: {t.id_transaction} | {t.description} | Monto: {t.amount} | De: {t.id_from_account} → A: {t.id_to_account}")
    
    def clear_entries(self):
        self.entry_amount.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_from_account.delete(0, tk.END)
        self.entry_to_account.delete(0, tk.END)
        self.entry_transaction_type.delete(0, tk.END)