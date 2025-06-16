# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY instalacion.txt .

# Instalar las dependencias (usa --no-cache-dir para ahorrar espacio)
RUN pip install --no-cache-dir -r instalacion.txt

# Copiar el resto del código al contenedor
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
