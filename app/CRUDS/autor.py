from sqlalchemy.orm import Session

from ..models import Asociacion


def create_autor(session: Session, nombre: str):
    Asociacion = Asociacion(nombre=nombre)
    session.add(Asociacion)
    session.commit()
    return Asociacion


def get_autores(session: Session):
    return session.query(Asociacion).all()


def get_autor(session: Session, autor_id: int):
    return session.get(Asociacion, autor_id)


def update_autor(session: Session, autor_id: int, nombre: str):
    Asociacion = session.get(Asociacion, autor_id)
    if Asociacion:
        Asociacion.nombre = nombre
        session.commit()
    return Asociacion


def delete_autor(session: Session, autor_id: int):
    Asociacion = session.get(Asociacion, autor_id)
    if Asociacion:
        session.delete(Asociacion)
        session.commit()
        return Asociacion
    return None