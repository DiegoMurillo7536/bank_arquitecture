from db_connection.connection import engine
from models.orm.account_type import AccountType

# Crear solo las tablas clients y accounts

AccountType.__table__.create(bind=engine)
print("Tabla tipos de cuentas creada")