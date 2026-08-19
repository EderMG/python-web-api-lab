# API de Gestión de Clientes en Python

Proyecto educativo para aprender **FastAPI**, un framework moderno para construir APIs en Python. 

Este proyecto implementa un **CRUD completo** (Create, Read, Update, Delete) con validación de datos, estructura profesional y buenas prácticas.

---

## 🎯 ¿Qué es un CRUD?

**CRUD** son las 4 operaciones básicas:

- **C** (Create) - Crear nuevos registros con `POST`
- **R** (Read) - Leer registros con `GET`
- **U** (Update) - Actualizar registros con `PUT`
- **D** (Delete) - Eliminar registros con `DELETE`

---

## 📋 Endpoints disponibles

### 📖 GET - Leer datos

| Endpoint | Descripción |
|----------|-------------|
| `GET /clientes` | Obtiene todos los clientes |
| `GET /clientes/{id}` | Obtiene un cliente por su ID |

### ➕ POST - Crear datos

| Endpoint | Descripción |
|----------|-------------|
| `POST /clientes` | Crea un nuevo cliente |

**Body (JSON):**
```json
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "edad": 30,
  "activo": true
}
```

### ✏️ PUT - Actualizar datos

| Endpoint | Descripción |
|----------|-------------|
| `PUT /clientes/{id}` | Actualiza un cliente existente |

**Body (JSON - todos opcionales):**
```json
{
  "nombre": "Juan Pérez Actualizado",
  "email": "juan.nuevo@example.com",
  "edad": 31,
  "activo": false
}
```

### 🗑️ DELETE - Eliminar datos

| Endpoint | Descripción |
|----------|-------------|
| `DELETE /clientes/{id}` | Elimina un cliente |

---

## 📂 Estructura del proyecto

```
WebAPI/
├── app/
│   ├── __init__.py           # Marca carpeta como paquete Python
│   ├── main.py               # Aplicación principal FastAPI
│   ├── models.py             # Modelos de datos (ClienteDB)
│   ├── schemas.py            # Esquemas de validación (Pydantic)
│   └── routes.py             # Endpoints CRUD
├── tests/
│   └── test_clients.py       # Pruebas de todos los endpoints
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

### 📝 Explicación de carpetas

- **app/main.py** - Aplicación principal. Configura FastAPI, CORS y registra las rutas
- **app/models.py** - Lógica de datos. Clase `ClienteDB` que simula una base de datos
- **app/schemas.py** - Validación con Pydantic. Define qué datos son válidos
- **app/routes.py** - Todos los endpoints CRUD organizados y documentados
- **tests/** - Pruebas automáticas para verificar que todo funciona

---

## 🚀 Instalación y ejecución

### 1) Instalar Python

Desde https://www.python.org/downloads/ o con:

```powershell
winget install --id Python.Python.3.12 -e
```

### 2) Crear entorno virtual

```powershell
cd "D:\Proyects\Peronales\Learning Python\WebAPI"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Instalar dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Ejecutar la API

```powershell
uvicorn app.main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

---

## 🧪 Probar la API

### Desde el navegador (GET)

```text
http://127.0.0.1:8000/clientes
http://127.0.0.1:8000/clientes/1
```

### Desde la documentación interactiva

```text
http://127.0.0.1:8000/docs
```

Aquí puedes probar todos los endpoints de forma visual.

### Desde la terminal (POST, PUT, DELETE)

```powershell
# Crear cliente
curl -X POST "http://127.0.0.1:8000/clientes" `
  -H "Content-Type: application/json" `
  -d '{"nombre":"Juan","email":"juan@example.com","edad":30,"activo":true}'

# Obtener cliente
curl "http://127.0.0.1:8000/clientes/1"

# Actualizar cliente
curl -X PUT "http://127.0.0.1:8000/clientes/1" `
  -H "Content-Type: application/json" `
  -d '{"nombre":"Juan Actualizado"}'

# Eliminar cliente
curl -X DELETE "http://127.0.0.1:8000/clientes/1"
```

### Ejecutar pruebas automáticas

```powershell
pytest -v
```

---

## 🔍 Conceptos clave que aprendes

### 1) **FastAPI**
- Crear aplicaciones web rápidas y modernas
- Usar decoradores `@app.get()`, `@app.post()`, etc.

### 2) **Pydantic**
- Validar datos automáticamente
- Definir esquemas de entrada/salida

### 3) **Estructura profesional**
- Separar lógica de datos (models)
- Separar validación (schemas)
- Separar endpoints (routes)

### 4) **HTTP Methods**
- GET - recuperar datos
- POST - crear datos
- PUT - actualizar datos
- DELETE - eliminar datos

### 5) **Status Codes HTTP**
- 200 - OK
- 201 - Created
- 204 - No Content
- 404 - Not Found
- 422 - Unprocessable Entity

---

## 💡 Próximos pasos

1. **Agregar base de datos real**
   - Usar SQLite, PostgreSQL o MongoDB en lugar de listas en memoria

2. **Agregar autenticación**
   - Proteger endpoints con tokens JWT

3. **Agregar más validaciones**
   - Verificar que el email sea único
   - Validar formato de datos más estricto

4. **Agregar paginación**
   - Limitación de resultados: `GET /clientes?skip=0&limit=10`

5. **Agregar búsqueda y filtros**
   - `GET /clientes?nombre=Juan&activo=true`

6. **Deploying a producción**
   - Usar Gunicorn con uvicorn
   - Desplegar en Heroku, Azure, AWS, etc.

---

## 📖 Recursos útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc9110.html#status.codes)
- [RESTful API Best Practices](https://restfulapi.net/)

---

**¡Esmerate aprendiendo FastAPI! 🚀**

gdfgdfg
gdf
gdf
gfdgdf}

gdfgdfg
gdf