# Agenda de Contactos v2

API REST construida con FastAPI y SQLAlchemy como proyecto de aprendizaje backend.

## Tecnologías
- Python 3.14
- FastAPI
- SQLAlchemy
- PostgreSQL
- HTML + JavaScript (frontend básico)

## Qué aprendí con este proyecto
- Conexión entre frontend y backend via fetch y JSON
- Modelado de base de datos con SQLAlchemy y Pydantic
- Diseño de endpoints REST con FastAPI
- Manejo de sesiones de base de datos y validación de datos

## Cómo correr el proyecto

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar el archivo `.env` con las credenciales de la base de datos
4. Correr el servidor: `python -m uvicorn main:app --reload`
5. Abrir `http://127.0.0.1:8000/docs` para ver la documentación
6. O abrir `http://127.0.0.1:8000/static/index.html` para el frontend

## Variables de entorno

Crear un archivo `.env` con:
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /contactos/ | Listar todos los contactos |
| GET | /contactos/buscar?nombre= | Buscar por nombre |
| POST | /contactos/ | Crear contacto |
| PATCH | /contactos/{id} | Actualizar contacto |
| DELETE | /contactos/{id} | Eliminar contacto |