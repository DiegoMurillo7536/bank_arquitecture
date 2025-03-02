from db_connection.connection import SessionLocal
from models.orm.transaction import Transaction

class TransactionRepository:
    """Maneja las consultas de la tabla transaction_type"""

    @staticmethod
    def get_all():
        """Obtiene todos los tipos de transacción"""
        with SessionLocal() as session:
            return session.query(Transaction).all()

    @staticmethod
    def get_by_id(transaction_type_id):
        """Busca un tipo de transacción por ID"""
        with SessionLocal() as session:
            return session.query(Transaction).filter_by(id_transaction_type=transaction_type_id).first()

    @staticmethod
    def create(amount,description,id_from_account,id_to_account,id_transaction_type):
        """Inserta un nuevo tipo de transacción"""
        with SessionLocal() as session:
            transaction = Transaction(
                amount=amount,
                description=description,
                id_from_account=id_from_account,
                id_to_account=id_to_account,
                id_transaction_type=id_transaction_type
            )
            session.add(transaction)
            session.commit()
            return transaction
