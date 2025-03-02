from db_connection.connection import engine
from models.orm.User import User
# Crear solo las tablas clients y accounts

User.__table__.create(bind=engine)
print("Tabla de User creada")