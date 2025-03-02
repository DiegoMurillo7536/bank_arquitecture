from db_connection.connection import SessionLocal
from models.orm.account_type import AccountType

class AccountTypeRepository:
    """Maneja las consultas de la tabla transaction_type"""

    @staticmethod
    def get_all():
        """Obtiene todos los tipos de transacción"""
        with SessionLocal() as session:
            return session.query(AccountType).all()

    @staticmethod
    def get_by_id(account_type_id):
        """Busca un tipo de transacción por ID"""
        with SessionLocal() as session:
            return session.query(AccountType).filter_by(id_account_type=account_type_id).first()

    @staticmethod
    def create(label):
        """Inserta un nuevo tipo de transacción"""
        with SessionLocal() as session:
            new_type = AccountType(label=label)
            session.add(new_type)
            session.commit()
            return new_type
