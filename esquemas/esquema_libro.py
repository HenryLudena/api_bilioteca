from pydantic import BaseModel, Field
from typing import Optional


class libroBase(BaseModel):
    titulo: str
    autor: str
    anio: int
    num_paginas: Optional[int]


class CrearLibro(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    descripcion: str = Field(min_length=1)
    num_paginas: int = Field(gt=0)


class LibroOut(CrearLibro):
    id: int

    class Config:
        orm_mode = True
