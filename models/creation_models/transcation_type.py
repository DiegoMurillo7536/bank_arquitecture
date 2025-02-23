from db_connection.connection import engine
from models.orm.transaction_type import TransactionType

# Crear solo las tablas clients y accounts

TransactionType.__table__.create(bind=engine)
print("Tabla de transacciones creada")




