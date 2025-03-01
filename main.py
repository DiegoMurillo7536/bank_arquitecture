import tkinter as tk
from views.index import IndexIu
from views.transaction_type import TransactionTypeUI
from views.account_type import AccountTypeUI
from views.account import AccountUI
from views.transaction import TransactionUI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("400x300")

        # Contenedor de vistas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Diccionario de vistas
        self.frames = {}

        # Agregar las vistas a la aplicación
        for F in (IndexIu, TransactionTypeUI,AccountTypeUI, AccountUI, TransactionUI):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IndexIu)

    def show_frame(self, cont):
        """Muestra el frame dado en `cont`."""
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
