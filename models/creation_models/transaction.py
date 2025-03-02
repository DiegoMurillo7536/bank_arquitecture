from db_connection.connection import engine
from models.orm.transaction import Transaction

# Crear solo las tablas clients y accounts

Transaction.__table__.create(bind=engine)
print("Tabla de transacciones creada")