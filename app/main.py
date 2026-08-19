"""Aplicación principal de la API de Clientes con FastAPI."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Gestión de Clientes",
    description="API CRUD simple para aprender FastAPI en Python",
    version="2.0.0"
)

# Configurar CORS (permite llamadas desde cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar las rutas
app.include_router(router)


# Endpoint raíz para verificar que la API está funcionando
@app.get("/", tags=["info"])
def raiz():
    """Endpoint raíz para verificar que la API está funcionando."""
    return {
        "mensaje": "¡Bienvenido a la API de Clientes!",
        "versión": "2.0.0",
        "documentación": "http://127.0.0.1:8000/docs",
        "endpoints": [
            "GET /clientes - Obtener todos los clientes",
            "GET /clientes/{id} - Obtener cliente por ID",
            "POST /clientes - Crear nuevo cliente",
            "PUT /clientes/{id} - Actualizar cliente",
            "DELETE /clientes/{id} - Eliminar cliente"
        ]
    }


# Endpoint health check (útil para monitoreo)
@app.get("/health", tags=["info"])
def health_check():
    """Verifica que la API está activa."""
    return {"status": "ok"}
