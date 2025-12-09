# Imagen base ligera con Python 3.11
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#
# Copiar el proyecto completo
COPY src ./src
COPY notebooks ./notebooks
COPY data ./data

EXPOSE 8888