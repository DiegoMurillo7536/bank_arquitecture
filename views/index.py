import tkinter as tk
from views.transaction_type import TransactionTypeUI
from views.account_type import AccountTypeUI
from views.account import AccountUI
from views.transaction import TransactionUI
class IndexIu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Menú Principal", font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="Gestionar Tipos de Transacción",
                  command=lambda: controller.show_frame(TransactionTypeUI)).pack(pady=5)
        tk.Button(self, text="Gestionar Tipos de Cuentas",
                  command=lambda: controller.show_frame(AccountTypeUI)).pack(pady=5)
        
        tk.Button(self, text="Gestionar Cuentas bancarias",
                  command=lambda: controller.show_frame(AccountUI)).pack(pady=5)
        tk.Button(self, text="Gestionar Transacciones",
                  command=lambda: controller.show_frame(TransactionUI)).pack(pady=5)
        

        tk.Button(self, text="Salir", command=controller.quit).pack(pady=20)
