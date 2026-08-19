"""
GUÍA EDUCATIVA: Conceptos clave de la API

Este archivo explica los conceptos importantes para entender el proyecto.
"""

# ============= 1. SEPARACIÓN DE RESPONSABILIDADES =============

"""
El proyecto está organizado en varias capas:

    CLIENTE (navegador, curl, Postman)
         ↓
    app/main.py (entrada a la aplicación)
         ↓
    app/routes.py (endpoints/rutas)
         ↓
    app/schemas.py (validación de datos)
         ↓
    app/models.py (lógica de datos)

¿Por qué separar?
- main.py: Solo configura la app
- routes.py: Solo define qué hacer con cada request
- schemas.py: Solo valida entrada/salida
- models.py: Solo maneja los datos

Ventaja: Cada archivo tiene UNA responsabilidad → código más limpio y mantenible
"""


# ============= 2. PYDANTIC Y VALIDACIÓN =============

"""
Pydantic es una librería que valida datos automáticamente.

Sin Pydantic (manual):
    def crear_cliente(data):
        if not isinstance(data, dict):
            raise ValueError("Debe ser un diccionario")
        if not isinstance(data['nombre'], str):
            raise ValueError("nombre debe ser string")
        if len(data['nombre']) < 1:
            raise ValueError("nombre no puede estar vacío")
        if '@' not in data['email']:
            raise ValueError("email inválido")
        # ... más validaciones ...
        return crear_en_db(data)

Con Pydantic:
    from pydantic import BaseModel, EmailStr, Field
    
    class ClienteCrear(BaseModel):
        nombre: str = Field(..., min_length=1, max_length=100)
        email: EmailStr  # Valida automáticamente
        edad: int = Field(..., ge=18, le=120)
        activo: bool = Field(default=True)
    
    def crear_cliente(cliente_data: ClienteCrear):
        return crear_en_db(cliente_data)

¿Ventajas?
- Código más limpio y legible
- Validación automática
- Documentación clara de qué se espera
- FastAPI genera documentación automáticamente
"""


# ============= 3. HTTP METHODS Y STATUS CODES =============

"""
GET - Obtener datos (seguro, no modifica)
    ✓ Usar para leer datos
    ✓ Sin cuerpo en el request
    Status codes comunes: 200, 404

POST - Crear datos (no seguro)
    ✓ Usar para crear nuevos registros
    ✓ Llevar datos en el body
    Status codes comunes: 201 (Created), 400, 422

PUT - Actualizar datos (no seguro)
    ✓ Usar para actualizar registros completos
    ✓ Llevar datos en el body
    Status codes comunes: 200, 404, 422

DELETE - Eliminar datos (no seguro)
    ✓ Usar para eliminar registros
    ✓ Sin cuerpo necesario
    Status codes comunes: 204 (No Content), 404

Status Codes importantes:
    200 OK              → Éxito, devuelve datos
    201 Created         → Éxito, recurso creado
    204 No Content      → Éxito, sin datos en respuesta
    400 Bad Request     → Error del cliente (datos mal formados)
    404 Not Found       → Recurso no encontrado
    422 Unprocessable   → Error de validación de datos
    500 Server Error    → Error del servidor
"""


# ============= 4. CLIENTE MOCK VS CLIENTE REAL =============

"""
En este proyecto usamos una lista en memoria (mock):

    CLIENTES_DB = [
        {"id": 1, "nombre": "Ana", ...},
        {"id": 2, "nombre": "Luis", ...}
    ]

¿Qué significa "mock"?
    Mock = simulación/falso. Usamos una lista simple en lugar de una BD real.

¿Por qué?
    ✓ Es simple de entender
    ✓ No necesita instalar BD
    ✓ Ideal para aprender
    ✓ Fácil de modificar

¿Qué pasa cuando reinicia la app?
    ✗ Se pierden los datos (porque la lista está en memoria)
    ✓ En una BD real, los datos persisten

Cuando entiendas bien el concepto, puedes reemplazar ClienteDB por:
    - SQLite (BD local simple)
    - PostgreSQL (BD profesional)
    - MongoDB (BD NoSQL)
    - Cualquier otra BD
"""


# ============= 5. DECORADORES EN FASTAPI =============

"""
Los decoradores son las líneas que comienzan con @

@app.get("/ruta")
def funcion():
    return {...}

¿Qué significa?
    Le dices a FastAPI: "Cuando alguien haga GET a /ruta, ejecuta esta función"

Ejemplos:
    @app.get("/clientes")         → GET http://api.com/clientes
    @app.post("/clientes")        → POST http://api.com/clientes
    @app.put("/clientes/{id}")    → PUT http://api.com/clientes/5
    @app.delete("/clientes/{id}") → DELETE http://api.com/clientes/5

¿Por qué @app.get() en lugar de @app.post()?
    Porque GET y POST son métodos HTTP diferentes que significan cosas distintas:
    - GET = leer (seguro, sin efectos secundarios)
    - POST = crear (modifica el servidor)
"""


# ============= 6. PARÁMETROS EN FASTAPI =============

"""
FastAPI detecta automáticamente qué son los parámetros:

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    return ClienteDB.obtener_por_id(cliente_id)

¿Qué pasa aquí?
    - cliente_id: int  → FastAPI sabe que es un parámetro de ruta (path parameter)
    - Valida que sea un número entero
    - Si no lo es, devuelve error 422

Tipos de parámetros:
    1. Path parameters (en la ruta)
        @app.get("/clientes/{id}")      → /clientes/5
    
    2. Query parameters (después de ?)
        @app.get("/clientes")
        def obtener(skip: int = 0, limit: int = 10)
        → /clientes?skip=5&limit=20
    
    3. Body parameters (en el JSON)
        @app.post("/clientes")
        def crear(cliente: ClienteCrear)  → POST con JSON en el body
"""


# ============= 7. CORS =============

"""
CORS = Cross-Origin Resource Sharing

¿Qué es?
    Mecanismo de seguridad de los navegadores que evita que una web
    haga requests a un servidor diferente.

Ejemplo:
    Navegador: http://localhost:3000
    API: http://localhost:8000
    
    Sin CORS:
        ✗ La web NO puede hacer requests a la API
    
    Con CORS activado:
        ✓ La web SI puede hacer requests a la API

En nuestro proyecto:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permite ANY origen
    )

En producción:
    allow_origins=["https://mi-web.com"]  # Solo permite tu sitio web
"""


# ============= 8. TESTING =============

"""
¿Por qué hacer pruebas?
    - Verificar que la API funciona
    - Detectar bugs temprano
    - Asegurarse que cambios no rompan nada
    - Documentar cómo debería funcionar

Estructura de una prueba:
    def test_obtener_cliente_por_id():
        # 1. SETUP: preparar el test
        response = client.get("/clientes/1")
        
        # 2. ACT: ejecutar la acción (ya hecho arriba)
        
        # 3. ASSERT: verificar el resultado
        assert response.status_code == 200
        assert response.json()["id"] == 1

Ejecutar pruebas:
    pytest               # Ejecuta todas
    pytest -v           # Con más detalles
    pytest test_clients.py::test_obtener_cliente_por_id  # Una específica
"""


# ============= 9. ASYNC/AWAIT (Adelanto) =============

"""
FastAPI soporta tanto funciones normales como async.

Normal (síncrono):
    @app.get("/clientes")
    def obtener_clientes():
        return ClienteDB.obtener_todos()

Async (asíncrono):
    @app.get("/clientes")
    async def obtener_clientes():
        return await ClienteDB.obtener_todos()

¿Cuándo usar async?
    - Cuando haces operaciones lentas (conexión a BD, APIs externas)
    - Permite manejar múltiples requests en paralelo
    - En este proyecto no es necesario (datos en memoria)

De momento, usa las funciones normales. Aprende async después.
"""


# ============= 10. PRÓXIMOS PASOS RECOMENDADOS =============

"""
1. Entiende bien los 4 endpoints CRUD
2. Prueba cada uno en http://127.0.0.1:8000/docs
3. Ejecuta pytest para ver que todo funciona
4. Intenta agregar un nuevo campo a Cliente
5. Aprende SQLAlchemy para conectar una BD real
6. Aprende async/await para mejor rendimiento
7. Aprende autenticación JWT para proteger endpoints
8. Despliega en Azure, Heroku o AWS

¡Esmerate! 🚀
"""
