"""Modelos de datos internos de la aplicación."""
from typing import Any, Dict, List


class ClienteDB:
    """Simula una base de datos simple en memoria."""
    
    # Almacenamiento en memoria de clientes
    clientes_db: List[Dict[str, Any]] = [
        {"id": 1, "nombre": "Ana García", "email": "ana@example.com", "edad": 29, "activo": True},
        {"id": 2, "nombre": "Luis Pérez", "email": "luis@example.com", "edad": 35, "activo": True},
        {"id": 3, "nombre": "María López", "email": "maria@example.com", "edad": 41, "activo": False},
        {"id": 4, "nombre": "Carlos Ruiz", "email": "carlos@example.com", "edad": 27, "activo": True},
    ]
    
    @staticmethod
    def obtener_todos() -> List[Dict[str, Any]]:
        """Devuelve todos los clientes."""
        return ClienteDB.clientes_db
    
    @staticmethod
    def obtener_por_id(cliente_id: int) -> Dict[str, Any] | None:
        """Busca un cliente por su ID."""
        for cliente in ClienteDB.clientes_db:
            if cliente["id"] == cliente_id:
                return cliente
        return None
    
    @staticmethod
    def crear(nombre: str, email: str, edad: int, activo: bool = True) -> Dict[str, Any]:
        """Crea un nuevo cliente."""
        # Calcula el siguiente ID
        nuevo_id = max([c["id"] for c in ClienteDB.clientes_db], default=0) + 1
        
        nuevo_cliente = {
            "id": nuevo_id,
            "nombre": nombre,
            "email": email,
            "edad": edad,
            "activo": activo
        }
        ClienteDB.clientes_db.append(nuevo_cliente)
        return nuevo_cliente
    
    @staticmethod
    def actualizar(cliente_id: int, nombre: str | None = None, email: str | None = None, 
                   edad: int | None = None, activo: bool | None = None) -> Dict[str, Any] | None:
        """Actualiza un cliente existente."""
        cliente = ClienteDB.obtener_por_id(cliente_id)
        if not cliente:
            return None
        
        # Solo actualiza los campos que se proporcionen
        if nombre is not None:
            cliente["nombre"] = nombre
        if email is not None:
            cliente["email"] = email
        if edad is not None:
            cliente["edad"] = edad
        if activo is not None:
            cliente["activo"] = activo
        
        return cliente
    
    @staticmethod
    def eliminar(cliente_id: int) -> bool:
        """Elimina un cliente por su ID."""
        for i, cliente in enumerate(ClienteDB.clientes_db):
            if cliente["id"] == cliente_id:
                ClienteDB.clientes_db.pop(i)
                return True
        return False
