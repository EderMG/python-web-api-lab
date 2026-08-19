"""Rutas CRUD para la API de clientes."""
from fastapi import APIRouter, HTTPException, status
from typing import List

from app.models import ClienteDB
from app.schemas import ClienteCrear, ClienteRespuesta, ClienteActualizar

# Crear el router
router = APIRouter(
    prefix="/clientes",
    tags=["clientes"],
    responses={404: {"description": "Cliente no encontrado"}}
)


# ============= ENDPOINTS GET =============

@router.get("", response_model=List[ClienteRespuesta])
def obtener_todos_clientes():
    """
    Obtiene todos los clientes.
    
    **Respuesta:** Lista de clientes con todos sus datos.
    """
    return ClienteDB.obtener_todos()


@router.get("/{cliente_id}", response_model=ClienteRespuesta)
def obtener_cliente_por_id(cliente_id: int):
    """
    Obtiene un cliente específico por su ID.
    
    **Parámetro:**
    - `cliente_id`: ID único del cliente
    
    **Respuestas:**
    - 200: Cliente encontrado
    - 404: Cliente no existe
    """
    cliente = ClienteDB.obtener_por_id(cliente_id)
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )
    
    return cliente


# ============= ENDPOINTS POST =============

@router.post("", response_model=ClienteRespuesta, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente_data: ClienteCrear):
    """
    Crea un nuevo cliente.
    
    **Body:**
    - `nombre`: Nombre completo (1-100 caracteres)
    - `email`: Email válido
    - `edad`: Edad entre 18 y 120 años
    - `activo`: Activo por defecto (opcional)
    
    **Respuesta:**
    - 201: Cliente creado exitosamente con su nuevo ID
    """
    nuevo_cliente = ClienteDB.crear(
        nombre=cliente_data.nombre,
        email=cliente_data.email,
        edad=cliente_data.edad,
        activo=cliente_data.activo
    )
    
    return nuevo_cliente


# ============= ENDPOINTS PUT =============

@router.put("/{cliente_id}", response_model=ClienteRespuesta)
def actualizar_cliente(cliente_id: int, cliente_data: ClienteActualizar):
    """
    Actualiza un cliente existente.
    
    **Parámetro:**
    - `cliente_id`: ID del cliente a actualizar
    
    **Body (todos opcionales):**
    - `nombre`: Nuevo nombre
    - `email`: Nuevo email
    - `edad`: Nueva edad
    - `activo`: Cambiar estado
    
    **Respuestas:**
    - 200: Cliente actualizado
    - 404: Cliente no existe
    """
    cliente = ClienteDB.actualizar(
        cliente_id,
        nombre=cliente_data.nombre,
        email=cliente_data.email,
        edad=cliente_data.edad,
        activo=cliente_data.activo
    )
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )
    
    return cliente


# ============= ENDPOINTS DELETE =============

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: int):
    """
    Elimina un cliente.
    
    **Parámetro:**
    - `cliente_id`: ID del cliente a eliminar
    
    **Respuestas:**
    - 204: Cliente eliminado exitosamente
    - 404: Cliente no existe
    """
    fue_eliminado = ClienteDB.eliminar(cliente_id)
    
    if not fue_eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )
