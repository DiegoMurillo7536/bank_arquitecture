from db_connection.connection import engine
from models.orm.account import Account

# Crear solo las tablas clients y accounts

Account.__table__.create(bind=engine)
print("Tabla de transacciones creada")




