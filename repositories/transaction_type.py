from db_connection.connection import SessionLocal
from models.orm.transaction_type import TransactionType

class TransactionTypeRepository:
    """Maneja las consultas de la tabla transaction_type"""

    @staticmethod
    def get_all():
        """Obtiene todos los tipos de transacción"""
        with SessionLocal() as session:
            return session.query(TransactionType).all()

    @staticmethod
    def get_by_id(transaction_type_id):
        """Busca un tipo de transacción por ID"""
        with SessionLocal() as session:
            return session.query(TransactionType).filter_by(id_transaction_type=transaction_type_id).first()

    @staticmethod
    def create(label):
        """Inserta un nuevo tipo de transacción"""
        with SessionLocal() as session:
            new_type = TransactionType(label=label)
            session.add(new_type)
            session.commit()
            return new_type
