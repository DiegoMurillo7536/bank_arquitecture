from sqlalchemy import Column, Integer, String, DateTime
from db_connection.connection import Base
from datetime import datetime

class TransactionType(Base):
    __tablename__ = "transaction_type"
    id_transaction_type = Column(Integer, primary_key=True)
    label = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)