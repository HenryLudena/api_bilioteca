#Pruebas de integración:
from fastapi.testclient import TestClient

from main import app

import sys
import os

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hello World"}
    
def test_crear_libro():
    nuevo_libro = {
    "num_paginas": 105,
    "titulo": "Libro ejemplo",
    "autor": "Autor ejemplo",
    "descripcion": "Descripcion ejemplo"
  }
    response = client.post("/libros/crear", json=nuevo_libro)
    assert response.status_code == 200
    # assert "insertado correctamente" in response.json()["mensaje"]