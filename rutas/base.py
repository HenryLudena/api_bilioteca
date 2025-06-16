from fastapi import APIRouter
from rutas import libros

api_router = APIRouter()

api_router.include_router(libros.router, prefix="/libros", tags=["libros"])
