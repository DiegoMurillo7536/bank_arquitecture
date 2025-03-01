import tkinter as tk
from tkinter import messagebox
from repositories.transaction_type import TransactionTypeRepository

class TransactionTypeUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#aed6f1")

        # Campo de entrada
        tk.Label(self, text="Nombre del Tipo de Transacción:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_label = tk.Entry(self, width=30)
        self.entry_label.grid(row=0, column=1, padx=10, pady=10)

        # Botón para agregar
        self.add_button = tk.Button(self, text="Agregar", command=self.add_transaction_type)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Lista de tipos de transacción
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)         

        # Cargar tipos de transacción
        self.load_transaction_types()

    def add_transaction_type(self):      
        label = self.entry_label.get().strip()
        if not label:
            messagebox.showwarning("Advertencia", "El campo no puede estar vacío")
            return

        TransactionTypeRepository.create(label)
        self.entry_label.delete(0, tk.END)
        self.load_transaction_types()
        messagebox.showinfo("Éxito", f"'{label}' agregado correctamente.")

    def load_transaction_types(self):
        self.listbox.delete(0, tk.END)
        transaction_types = TransactionTypeRepository.get_all()
        for t in transaction_types:
            self.listbox.insert(tk.END, f"{t.id_transaction_type}: {t.label}")
