from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from db_connection.connection import Base
from models.orm.account_type import AccountType
from datetime import datetime

class Account(Base):
    __tablename__ = "account"
    id_account = Column(Integer, primary_key=True)
    label = Column(String(50), nullable=False)
    is_exempt = Column(Boolean, nullable=False)
    account_type_id = Column(Integer,ForeignKey(AccountType.id_account_type), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)