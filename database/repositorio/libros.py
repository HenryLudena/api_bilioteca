from sqlalchemy.orm import Session
from esquemas.esquema_libro import CrearLibro
from database.modelos.modelo_libro import Libro


def crear_nuevo_libro(libro: CrearLibro, db: Session):
    objeto_libro = Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        descripcion=libro.descripcion,
        num_paginas=libro.num_paginas,
    )
    db.add(objeto_libro)
    db.commit()
    db.refresh(objeto_libro)
    return objeto_libro


def listar_libros(db: Session):
    libros = db.query(Libro).all()
    return libros


def listar_libros_id(id: int, db: Session):
    libro = db.query(Libro).filter(Libro.id == id).first()
    return libro


def actualizar_libro(id: int, libro: CrearLibro, db: Session):
    objeto_libro = db.query(Libro).filter(Libro.id == id).first()
    objeto_libro.titulo = libro.titulo
    objeto_libro.autor = libro.autor
    objeto_libro.descripcion = libro.descripcion
    objeto_libro.num_paginas = libro.num_paginas
    db.commit()
    db.refresh(objeto_libro)
    return objeto_libro


def eliminar_libro(id: int, db: Session):
    libro = db.query(Libro).filter(Libro.id == id).first()
    db.delete(libro)
    db.commit()
    return {libro.titulo + " ha sido eliminado"}
