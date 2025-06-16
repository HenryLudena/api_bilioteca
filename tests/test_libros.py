#Pruebas de integración:
from fastapi.testclient import TestClient

from main import app

import sys
import os

# Añadir la carpeta raíz del proyecto al path de importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hello World"}
    
def test_crear_libro():
    nuevo_libro = {
        "titulo": "Crimen y Castigo",
        "autor": "Dostoievski",
        "anio": 1866
    }
    response = client.post("/libros/crear", json=nuevo_libro)
    assert response.status_code == 200
    # assert "insertado correctamente" in response.json()["mensaje"]