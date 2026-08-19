from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# ============= Tests GET =============

def test_obtener_todos_clientes():
    """Verifica que se obtengan todos los clientes."""
    response = client.get("/clientes")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 4  # Al menos los 4 clientes iniciales


def test_obtener_cliente_por_id():
    """Verifica que se obtenga un cliente por su ID."""
    response = client.get("/clientes/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["nombre"] == "Ana García"


def test_obtener_cliente_no_existe():
    """Verifica que devuelva 404 si el cliente no existe."""
    response = client.get("/clientes/99999")
    
    assert response.status_code == 404


# ============= Tests POST =============

def test_crear_cliente():
    """Verifica que se puede crear un nuevo cliente."""
    nuevo_cliente = {
        "nombre": "Juan Nuevo",
        "email": "juan@example.com",
        "edad": 30,
        "activo": True
    }
    
    response = client.post("/clientes", json=nuevo_cliente)
    
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Juan Nuevo"
    assert data["email"] == "juan@example.com"
    assert "id" in data  # Debe tener un ID asignado


def test_crear_cliente_email_invalido():
    """Verifica que rechaza emails inválidos."""
    nuevo_cliente = {
        "nombre": "Juan",
        "email": "no-es-email",  # Email inválido
        "edad": 30,
        "activo": True
    }
    
    response = client.post("/clientes", json=nuevo_cliente)
    
    assert response.status_code == 422  # Unprocessable Entity


def test_crear_cliente_edad_invalida():
    """Verifica que rechaza edades fuera del rango."""
    nuevo_cliente = {
        "nombre": "Juan",
        "email": "juan@example.com",
        "edad": 15,  # Menor a 18
        "activo": True
    }
    
    response = client.post("/clientes", json=nuevo_cliente)
    
    assert response.status_code == 422


# ============= Tests PUT =============

def test_actualizar_cliente():
    """Verifica que se puede actualizar un cliente."""
    datos_actualizados = {
        "nombre": "Ana García Actualizada",
        "email": "ana.nueva@example.com",
        "edad": 30,
        "activo": False
    }
    
    response = client.put("/clientes/1", json=datos_actualizados)
    
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Ana García Actualizada"
    assert data["activo"] is False


def test_actualizar_cliente_parcial():
    """Verifica que se puede actualizar solo algunos campos."""
    datos_parciales = {
        "nombre": "Ana García Parcial"
    }
    
    response = client.put("/clientes/1", json=datos_parciales)
    
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Ana García Parcial"


def test_actualizar_cliente_no_existe():
    """Verifica que devuelve 404 al actualizar cliente inexistente."""
    response = client.put("/clientes/99999", json={"nombre": "Test"})
    
    assert response.status_code == 404


# ============= Tests DELETE =============

def test_eliminar_cliente():
    """Verifica que se puede eliminar un cliente."""
    # Primero crea un cliente para eliminar
    nuevo_cliente = {
        "nombre": "Cliente a Eliminar",
        "email": "eliminar@example.com",
        "edad": 25
    }
    create_response = client.post("/clientes", json=nuevo_cliente)
    cliente_id = create_response.json()["id"]
    
    # Luego lo elimina
    response = client.delete(f"/clientes/{cliente_id}")
    
    assert response.status_code == 204
    
    # Verifica que ya no existe
    check_response = client.get(f"/clientes/{cliente_id}")
    assert check_response.status_code == 404


def test_eliminar_cliente_no_existe():
    """Verifica que devuelve 404 al eliminar cliente inexistente."""
    response = client.delete("/clientes/99999")
    
    assert response.status_code == 404


# ============= Tests Endpoints Info =============

def test_raiz():
    """Verifica que el endpoint raíz devuelve info de la API."""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "mensaje" in data
    assert "versión" in data


def test_health_check():
    """Verifica que el health check funciona."""
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
