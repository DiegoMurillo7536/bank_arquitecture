from db_connection.connection import SessionLocal
from models.orm.account import Account

class AccountRepository:
    """Maneja las consultas de la tabla transaction_type"""

    @staticmethod
    def get_all():
        """Obtiene todos los tipos de transacción"""
        with SessionLocal() as session:
            return session.query(Account).all()

    @staticmethod
    def get_by_id(id_account):
        """Busca un tipo de transacción por ID"""
        with SessionLocal() as session:
            return session.query(Account).filter_by(id_account=id_account).first()

    @staticmethod
    def create(label,is_exempt,account_type_id):
        """Inserta un nuevo tipo de transacción"""
        with SessionLocal() as session:
            new_account = Account(
                label=label,
                is_exempt=is_exempt,
                account_type_id=account_type_id
                )
            session.add(new_account)
            session.commit()
            return new_account
