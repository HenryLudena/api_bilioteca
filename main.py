# python3 -m venv biblioteca-env
# biblioteca-env/Scripts/activate.bat
# pip install fastapi
# pip install uvicorn

# uvicorn main:app --reload

from fastapi import FastAPI
from rutas.libros import libros_router

# Base de Datos
from database.base import Base
from database.sesion import engine
from database.modelos.modelo_libro import Libro


# Definir las rutas
def incluir_rutas(app):
    app.include_router(libros_router)


# Crear las tablas automáticamente:
def crear_tablas():
    Base.metadata.create_all(bind=engine)


# Iniciar la aplicación
def iniciar_aplicacion():
    app = FastAPI(title="Hola Mundo", version="0.0.1")
    incluir_rutas(app)
    crear_tablas()
    return app


app = iniciar_aplicacion()
