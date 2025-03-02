from sqlalchemy import Column, Integer, String, DateTime
from db_connection.connection import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"
    id_User_Documento = Column(Integer, primary_key=True)
    Nombre= Column(String(50), nullable=False)
    Nacionalidad= Column(String(50), nullable=False)
    EstadoCivil= Column(String(50), nullable=False)
    CorreoElectronico= Column(String(50), nullable=False)
    FechaNacimiento = Column(DateTime, default=datetime.now)

