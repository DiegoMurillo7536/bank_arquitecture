import tkinter as tk
from views.transaction_type import TransactionTypeUI

class IndexIu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Menú Principal", font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="Gestionar Tipos de Transacción",
                  command=lambda: controller.show_frame(TransactionTypeUI)).pack(pady=5)

        tk.Button(self, text="Salir", command=controller.quit).pack(pady=20)
