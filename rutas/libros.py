from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from esquemas.esquema_libro import CrearLibro, LibroOut
from database.sesion import get_db
from database.repositorio.libros import (
    crear_nuevo_libro,
    listar_libros,
    listar_libros_id,
    actualizar_libro,
    eliminar_libro,
)

# uvicorn rutas/libros:app --reload
libros_router = APIRouter()

# Ruta: http://127.0.0.1:8000


@libros_router.get(
    "/"
)  # FASTAPI: registra la función (la función que aparece en el directorio raíz)
def index():
    return {"mensaje": "Hello World"}


# id: parámetro variable
# @libros_router.get("/libros/{id}")
# def mostrar_libro(id: int):
#    return {"data":id}

# BaseModel: Garantiza validación datos. Ej: id: int garantiza que sea int


# @libros_router.post("/libros")
# def insertar_libro(libro: Libro):
#     return {"mensaje": f"Libro {libro.titulo} insertado correctamente"}


@libros_router.post("/libros/crear")
def crear_libro(libro: CrearLibro, db: Session = Depends(get_db)):
    libro = crear_nuevo_libro(libro=libro, db=db)
    return libro


@libros_router.get("/libros/todos")
def obtener_libros(db: Session = Depends(get_db)):
    libros = listar_libros(db=db)
    return libros


@libros_router.get("/libros/{id}")
def obtener_libro_id(id=int, db: Session = Depends(get_db)):
    libro = listar_libros_id(id=id, db=db)
    if not libro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro con id: " + str(id) + "no encontrado",
        )
    return libro


@libros_router.put("/libros/actualizar/{id}", response_model=LibroOut)
def actualizar_libro_handler(id: int, libro: CrearLibro, db: Session = Depends(get_db)):
    libro = actualizar_libro(id=id, libro=libro, db=db)
    if not libro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro con id: " + str(id) + "no encontrado",
        )
    return libro


@libros_router.delete("/libros/eliminar/{id}")
def eliminar_libro_handler(id: int, db: Session = Depends(get_db)):
    libro = eliminar_libro(id=id, db=db)
    if not libro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro con id: " + str(id) + "no encontrado",
        )
    return libro
