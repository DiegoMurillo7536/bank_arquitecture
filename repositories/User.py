from db_connection.connection import SessionLocal
from models.orm.User import User

class UserRepository:
    """Maneja las consultas de la tabla User"""

    @staticmethod
    def get_all(limit=10, offset=0):
        """Obtiene todos los usuarios con paginación"""
        with SessionLocal() as session:
            return session.query(User).offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(user_id):
        """Busca un usuario por ID"""
        with SessionLocal() as session:
            return session.query(User).filter_by(id_user=user_id).first()

    @staticmethod
    def create(nombre, nacionalidad, estado_civil, correo_electronico, fecha_nacimiento):
        """Inserta un nuevo usuario"""
        with SessionLocal() as session:
            try:
                new_user = User(
                    Nombre=nombre,
                    Nacionalidad=nacionalidad,
                    EstadoCivil=estado_civil,
                    CorreoElectronico=correo_electronico,
                    FechaNacimiento=fecha_nacimiento
                )
                session.add(new_user)
                session.commit()
                session.refresh(new_user)  # Para asegurarnos de obtener el ID asignado
                return new_user
            except Exception as e:
                session.rollback()
                raise e  # Relanza la excepción para que pueda manejarse en otro nivel