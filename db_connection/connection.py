import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user_name = os.getenv("USER_POSTRES_NAME")
user_password = os.getenv("USER_POSTRES_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
# Configuración de la conexión a PostgreSQL
DATABASE_URL = f"postgresql://{user_name}:{user_password}@localhost:5432/{database_name}"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
