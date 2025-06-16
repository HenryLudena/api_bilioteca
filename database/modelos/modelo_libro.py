from sqlalchemy import Column, Integer, String

from database.base_class import Base


class Libro(Base):
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    descripcion = Column(String)
    num_paginas = Column(Integer)
