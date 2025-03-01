from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from db_connection.connection import Base
from datetime import datetime
from models.orm.account import Account
from models.orm.transaction_type import TransactionType

class Transaction(Base):
    __tablename__ = "transactions"
    id_transaction = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String(50), nullable=False)
    id_from_account = Column(Integer, ForeignKey(Account.id_account) ,nullable=False)
    id_to_account = Column(Integer, ForeignKey(Account.id_account), nullable=False)
    id_transaction_type = Column(Integer, ForeignKey(TransactionType.id_transaction_type), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)