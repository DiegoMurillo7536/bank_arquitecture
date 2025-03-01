import tkinter as tk
from views.transaction_type import TransactionTypeUI
from views.account_type import AccountTypeUI
from views.account import AccountUI
from views.transaction import TransactionUI
class IndexIu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#aed6f1")

        tk.Label(self, text="Menú Principal", bg="#aed6f1", fg="#333333", font=("Arial", 14)).pack(pady=20)

        button_style = {"relief": "groove", "bd": 5, "padx": 10, "pady": 5, "font": ("Arial", 12)}
        
        tk.Button(self, text="Gestionar Transacciones", bg="#FAD7A0", fg="#333333",
                  command=lambda: controller.show_frame(TransactionUI), **button_style).pack(pady=5)

        tk.Button(self, text="Gestionar Tipos de Transacción", bg="#FAD7A0", fg="#333333", 
                  command=lambda: controller.show_frame(TransactionTypeUI), **button_style).pack(pady=5)
                  
        tk.Button(self, text="Gestionar Tipos de Cuentas", bg="#FAD7A0", fg="#333333",
                  command=lambda: controller.show_frame(AccountTypeUI), **button_style).pack(pady=5)
                  
        tk.Button(self, text="Gestionar Cuentas bancarias", bg="#FAD7A0", fg="#333333",
                  command=lambda: controller.show_frame(AccountUI), **button_style).pack(pady=5)

        tk.Button(self, text="Salir", bg="#c0392b", fg="white", 
                  command=controller.quit, **button_style).pack(pady=20)