from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds import (
    create_jugador,
    get_jugador,
    get_jugadores,
    update_jugador,
    delete_jugador,
)

router = APIRouter()

@router.get("/")
def get_jugadores_endpoint(Session=Depends(get_db)):
    jugadores = get_jugadores(Session)
    return[
        {"id": j.id, "nombre": j.nombre, "pais": j.pais}
        for j in jugadores
    ]


@router.get("/{jugador_id}")
def get_jugador_endpoint(jugador_id:int, Session=Depends(get_db)):
    jugador = get_jugador(Session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador no encontrado")
    return{
        "id": jugador.id,
        "nombre": jugador.nombre,
        "pais": jugador.pais,
    }


@router.post("/")
def create_jugador_endpoint(jugador_id: int, nombre:str, pais:str, session=Depends(get_db)):
    jugador = create_jugador(session, jugador_id, nombre, pais)
    return{
        "id": jugador.id,
        "nombre": jugador.nombre,
        "pais": jugador.pais,
    }

@router.put("/{jugador_id}")
def update_jugador_endpoint(jugador_id:int, nombre:str, pais:str, session=Depends(get_db)):
    jugador = update_jugador(session, jugador_id, nombre, pais)
    return{
        "id": jugador.id,
        "nombre": jugador.nombre,
        "pais": jugador.pais,
    }

@router.delete("/{jugador_id}")
def delete_jugador_endpoint(jugador_id:int, session=Depends(get_db)):
    jugador = delete_jugador(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador not found")
    return{
        "detail": "jugador deleted successfully"
    }