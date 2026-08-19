"""
EJEMPLOS DE USO DE LA API

Este archivo contiene ejemplos de cómo usar cada endpoint de la API.
Puedes copiar y pegar estos comandos en tu terminal (PowerShell, bash, etc.)
"""

# ============= GET /clientes =============
# Obtiene todos los clientes

# Con curl
curl "http://127.0.0.1:8000/clientes"

# Respuesta esperada:
# [
#   {"id": 1, "nombre": "Ana García", "email": "ana@example.com", "edad": 29, "activo": true},
#   {"id": 2, "nombre": "Luis Pérez", "email": "luis@example.com", "edad": 35, "activo": true},
#   ...
# ]


# ============= GET /clientes/{id} =============
# Obtiene un cliente específico por su ID

curl "http://127.0.0.1:8000/clientes/1"

# Respuesta esperada:
# {"id": 1, "nombre": "Ana García", "email": "ana@example.com", "edad": 29, "activo": true}


# ============= POST /clientes =============
# Crea un nuevo cliente

curl -X POST "http://127.0.0.1:8000/clientes" `
  -H "Content-Type: application/json" `
  -d '{
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "edad": 30,
    "activo": true
  }'

# Respuesta esperada (con Status 201 Created):
# {"id": 5, "nombre": "Juan Pérez", "email": "juan@example.com", "edad": 30, "activo": true}


# ============= PUT /clientes/{id} =============
# Actualiza un cliente existente

# Actualizar todos los campos
curl -X PUT "http://127.0.0.1:8000/clientes/1" `
  -H "Content-Type: application/json" `
  -d '{
    "nombre": "Ana García Nueva",
    "email": "ana.nueva@example.com",
    "edad": 30,
    "activo": false
  }'

# Actualizar solo el nombre (los otros campos se mantienen)
curl -X PUT "http://127.0.0.1:8000/clientes/1" `
  -H "Content-Type: application/json" `
  -d '{
    "nombre": "Ana García Actualizada"
  }'

# Respuesta esperada:
# {"id": 1, "nombre": "Ana García Actualizada", "email": "ana@example.com", "edad": 29, "activo": true}


# ============= DELETE /clientes/{id} =============
# Elimina un cliente

curl -X DELETE "http://127.0.0.1:8000/clientes/1"

# Respuesta esperada (Status 204 No Content - sin cuerpo)


# ============= EJEMPLOS CON PYTHON (requests) =============

import requests

# URL base de la API
BASE_URL = "http://127.0.0.1:8000"

# GET - Obtener todos los clientes
response = requests.get(f"{BASE_URL}/clientes")
print(response.json())

# GET - Obtener cliente por ID
response = requests.get(f"{BASE_URL}/clientes/1")
print(response.json())

# POST - Crear nuevo cliente
nuevo_cliente = {
    "nombre": "María Nueva",
    "email": "maria@example.com",
    "edad": 25,
    "activo": True
}
response = requests.post(f"{BASE_URL}/clientes", json=nuevo_cliente)
print(f"Creado con status {response.status_code}")
print(response.json())

# PUT - Actualizar cliente
datos_actualizados = {
    "nombre": "María Actualizada",
    "edad": 26
}
response = requests.put(f"{BASE_URL}/clientes/1", json=datos_actualizados)
print(response.json())

# DELETE - Eliminar cliente
response = requests.delete(f"{BASE_URL}/clientes/1")
print(f"Eliminado con status {response.status_code}")


# ============= DOCUMENTACIÓN INTERACTIVA =============

# FastAPI genera documentación automática. Accede a:
# http://127.0.0.1:8000/docs (Swagger UI)
# http://127.0.0.1:8000/redoc (ReDoc)

# En estas páginas puedes probar todos los endpoints de forma visual
