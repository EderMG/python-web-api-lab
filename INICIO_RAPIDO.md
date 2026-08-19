"""
INICIO RÁPIDO - 5 MINUTOS

Guía mínima para arrancar la API en 5 minutos.
"""

# ============= PASO 1: Preparar entorno (2 min) =============

# Abre PowerShell en la carpeta del proyecto:
cd "D:\Proyects\Peronales\Learning Python\WebAPI"

# Crea entorno virtual:
python -m venv .venv

# Activa el entorno:
.\.venv\Scripts\Activate.ps1

# Si te pide permiso, ejecuta primero:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned


# ============= PASO 2: Instalar dependencias (2 min) =============

python -m pip install --upgrade pip
pip install -r requirements.txt

# Espera a que termine...


# ============= PASO 3: Ejecutar la API (1 min) =============

uvicorn app.main:app --reload

# Verás algo como:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Application startup complete


# ============= PASO 4: Abrir en el navegador =============

# Abre CUALQUIERA de estas URLs en tu navegador:

# 1. Documentación interactiva (MEJOR):
http://127.0.0.1:8000/docs

# 2. Ver clientes:
http://127.0.0.1:8000/clientes

# 3. Ver cliente específico:
http://127.0.0.1:8000/clientes/1


# ============= PROBAR ENDPOINTS EN /docs =============

# En http://127.0.0.1:8000/docs puedes:

# 1. Click en "GET /clientes"
# 2. Click en "Try it out"
# 3. Click en "Execute"
# 4. Ver respuesta abajo

# Haz lo mismo con POST, PUT, DELETE


# ============= EJECUTAR PRUEBAS =============

# En OTRA terminal PowerShell (mantén la API ejecutándose):

cd "D:\Proyects\Peronales\Learning Python\WebAPI"
.\.venv\Scripts\Activate.ps1
pytest -v

# Verás algo como:
# test_clients.py::test_obtener_todos_clientes PASSED     [12%]
# test_clients.py::test_obtener_cliente_por_id PASSED    [25%]
# ...


# ============= ARCHIVOS IMPORTANTES =============

# README.md                 → Documentación completa
# CONCEPTOS_CLAVE.md        → Explicación de conceptos
# EJEMPLOS_USO.md           → Ejemplos de uso con curl y Python
# app/main.py               → Archivo principal (revisá este!)
# app/routes.py             → Todos los endpoints
# app/models.py             → Lógica de datos
# app/schemas.py            → Validación de datos
# tests/test_clients.py     → Pruebas automáticas


# ============= DETENER LA API =============

# En la terminal donde está ejecutándose:
# Presiona Ctrl+C


# ¡Eso es todo! Ya tienes un CRUD funcionando 🚀
