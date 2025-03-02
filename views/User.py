import tkinter as tk
from tkinter import messagebox
from db_connection.connection import SessionLocal
from models.orm.User import User
from repositories.User import UserRepository

class UserUI(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.offset = 0
        self.limit = 10

        # Labels y Entradas
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Nacionalidad:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nacionalidad = tk.Entry(self, width=30)
        self.entry_nacionalidad.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Estado Civil:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_estado_civil = tk.Entry(self, width=30)
        self.entry_estado_civil.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Correo Electrónico:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_correo = tk.Entry(self, width=30)
        self.entry_correo.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Fecha de Nacimiento (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
        self.entry_fecha_nac = tk.Entry(self, width=30)
        self.entry_fecha_nac.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        self.add_button = tk.Button(self, text="Agregar", command=self.add_user)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)


        # Listbox para mostrar usuarios
        self.listbox = tk.Listbox(self, width=80, height=10)
        self.listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        self.load_users()

    def add_user(self):
        """Agrega un nuevo usuario a la base de datos."""
        nombre = self.entry_nombre.get().strip()
        nacionalidad = self.entry_nacionalidad.get().strip()
        estado_civil = self.entry_estado_civil.get().strip()
        correo = self.entry_correo.get().strip()
        fecha_nac = self.entry_fecha_nac.get().strip()

        if not all([nombre, nacionalidad, estado_civil, correo, fecha_nac]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        try:
            new_user = UserRepository.create(nombre, nacionalidad, estado_civil, correo, fecha_nac)
            self.load_users()
            messagebox.showinfo("Éxito", f"Usuario '{new_user.Nombre}' agregado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario: {str(e)}")

    def load_users(self):
        """Carga usuarios con paginación."""
        self.listbox.delete(0, tk.END)
        users = UserRepository.get_all(limit=self.limit, offset=self.offset)

        for user in users:
            self.listbox.insert(tk.END, f"{user.id_User_Documento}: {user.Nombre} | {user.CorreoElectronico}")

