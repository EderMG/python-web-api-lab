# 🚀 GUÍA COMPLETA: Desplegar FastAPI a Azure

## 📋 Requisitos Previos

Antes de desplegar, necesitas tener:

### 1) **Cuenta de Azure**
- Crear una cuenta en https://azure.microsoft.com/
- Puedes usar la cuenta de Microsoft (Outlook, Hotmail, etc.)
- **GRATIS:** $200 créditos durante 30 días

### 2) **Azure CLI instalado**
```powershell
# Instalar
winget install --id Microsoft.AzureCLI -e

# Verificar
az --version

# Loguearse
az login
```

Si `az login` abre el navegador, solo acepta en la pantalla que aparece. Eso es normal.

### 3) **Git instalado (opcional pero recomendado)**
```powershell
winget install --id Git.Git -e
```

### 4) **Tu proyecto en GitHub (opcional)**
Si quieres desplegar desde GitHub, crea un repositorio:
```powershell
git init
git add .
git commit -m "Initial commit"
git push origin main
```

---

## 🎯 Opciones de Servicio Azure para FastAPI

### Opción A: **Azure App Service** ⭐ RECOMENDADO (MÁS SIMPLE)

**¿Qué es?**
- Servicio administrado para aplicaciones web
- No necesitas gestionar servidores
- FastAPI se ejecuta directamente

**Ventajas:**
- ✅ Más simple de configurar
- ✅ Menos costo (€20-50/mes)
- ✅ Auto-escalado automático
- ✅ Monitoreo integrado
- ✅ Perfect para APIs pequeñas/medianas

**Desventajas:**
- ❌ Menos personalizable que Container Apps
- ❌ No ideal para cargas muy pesadas

**Costo:** ~€20-50/mes (tier B1)

---

### Opción B: **Azure Container Apps** (MÁS FLEXIBLE)

**¿Qué es?**
- Ejecuta la app en un contenedor Docker
- Más control y flexibilidad
- Escalado automático

**Ventajas:**
- ✅ Altamente escalable
- ✅ Control total del entorno
- ✅ Ideal para aplicaciones complejas
- ✅ Compatible con CI/CD avanzado

**Desventajas:**
- ❌ Más complejo de configurar
- ❌ Requiere Dockerfile
- ❌ Más caro (€30-80/mes)

**Costo:** ~€30-80/mes

---

### Opción C: **Azure Functions** (SIN SERVIDOR)

**¿Qué es?**
- Ejecuta código sin gestionar servidores
- Pago solo por ejecuciones

**Ventajas:**
- ✅ Muy barato (pay-per-use)
- ✅ Auto-escalado infinito
- ✅ Ideal para APIs simples

**Desventajas:**
- ❌ Requiere reescribir código a modelo Functions
- ❌ Timeout de 10 minutos
- ❌ Más complejo para FastAPI

**Costo:** ~€0-10/mes (muy bajo uso)

---

## 🏆 RECOMENDACIÓN

**Para esta API de clientes: Usa Azure App Service**

✅ Simple de usar  
✅ Costo bajo  
✅ Perfecto para aprender  
✅ Escala bien  

---

## 📊 Arquitectura de Despliegue

```
Tu máquina local
        ↓
    Git Push
        ↓
GitHub Repository (opcional)
        ↓
Azure App Service
        ↓
    FastAPI API
        ↓
Base de datos (SQLite en memoria o opcional: Azure SQL)
```

---

## 🔧 PASO A PASO: Azure App Service (Opción Recomendada)

### Fase 0: Preparar la Máquina Local

#### Paso 1: Instalar Azure CLI
```powershell
winget install --id Microsoft.AzureCLI -e
```

Cerrar y abrir una terminal nueva. Verificar:
```powershell
az --version
```

#### Paso 2: Loguear a Azure
```powershell
az login
```

Se abrirá un navegador. Solo acepta cuando pida confirmación.

Verificar que estás logueado:
```powershell
az account show
```

Deberías ver tu información de Azure.

---

### Fase 1: Preparar la App para Azure

#### Paso 3: Crear archivo `.gitignore` (si no existe)
```
.venv/
__pycache__/
*.pyc
.pytest_cache/
.env
```

#### Paso 4: Crear archivo `.env` local (para desarrollo)
```
ENVIRONMENT=development
DEBUG=true
```

**Nota:** En Azure, las variables se configuran en Azure Portal (NO en .env)

#### Paso 5: Crear archivo `Procfile` (solo para azd)
```
web: uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Este archivo le dice a Azure cómo iniciar tu app.

---

### Fase 2: Crear Recursos en Azure

#### Paso 6: Crear Grupo de Recursos
```powershell
$appName = "api-clientes"
$resourceGroup = "$appName-rg"
$region = "eastus"

az group create `
  --name $resourceGroup `
  --location $region

# Salida esperada:
# "location": "eastus",
# "name": "api-clientes-rg"
```

**¿Qué es?**
- Contenedor lógico para agrupar todos tus recursos

#### Paso 7: Crear Plan de App Service
```powershell
$appPlan = "$appName-plan"

az appservice plan create `
  --name $appPlan `
  --resource-group $resourceGroup `
  --sku B1 `
  --is-linux

# Salida esperada:
# "name": "api-clientes-plan",
# "sku": "B1 (Basic)"
```

**¿Qué es?**
- Define los recursos (CPU, RAM) para tu app
- B1 = suficiente para APIs pequeñas

#### Paso 8: Crear la Web App
```powershell
az webapp create `
  --resource-group $resourceGroup `
  --plan $appPlan `
  --name $appName `
  --runtime "PYTHON:3.12" `
  --runtime-version 3.12

# Salida esperada:
# "defaultHostName": "api-clientes.azurewebsites.net"
```

**¿Qué es?**
- Tu API estará en: https://api-clientes.azurewebsites.net

---

### Fase 3: Configurar la App Service

#### Paso 9: Configurar Comando de Inicio
```powershell
az webapp config set `
  --resource-group $resourceGroup `
  --name $appName `
  --startup-file "python -m uvicorn app.main:app --host 0.0.0.0"
```

Este comando le dice a Azure cómo iniciar FastAPI.

#### Paso 10: Habilitar Build Automático
```powershell
az webapp config appsettings set `
  --resource-group $resourceGroup `
  --name $appName `
  --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

Esto hace que Azure instale automáticamente las dependencias de `requirements.txt`.

---

### Fase 4: Desplegar el Código

#### Opción A: Desplegar desde archivo ZIP (más simple)

**Paso 11: Crear ZIP con el proyecto**
```powershell
# Desde PowerShell en la carpeta del proyecto
Compress-Archive -Path app, tests, requirements.txt, conftest.py, Procfile `
  -DestinationPath deploy.zip

# Verificar que se creó
ls deploy.zip
```

**Paso 12: Desplegar a Azure**
```powershell
az webapp deployment source config-zip `
  --resource-group $resourceGroup `
  --name $appName `
  --src deploy.zip

# Verás algo como:
# "URL": "https://api-clientes.azurewebsites.net"
```

**Paso 13: Esperar a que despliegue (2-3 minutos)**
```powershell
# Abrir logs en tiempo real
az webapp log tail `
  --resource-group $resourceGroup `
  --name $appName `
  --provider all

# Verás output como:
# 2024-08-14 10:30:45 Updating submodules...
# 2024-08-14 10:31:10 Running oryx build...
# ...
# 2024-08-14 10:32:00 Starting uvicorn...
```

---

#### Opción B: Desplegar desde GitHub (automático)

**Paso 11: Subir proyecto a GitHub**
```powershell
# En la carpeta del proyecto
git init
git add .
git commit -m "Initial commit: FastAPI CRUD"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/api-clientes.git
git push -u origin main
```

**Paso 12: Conectar GitHub a Azure**
```powershell
az webapp deployment github-actions add `
  --resource-group $resourceGroup `
  --name $appName `
  --repo TU_USUARIO/api-clientes `
  --branch main `
  --runtime "python"

# Salida esperada:
# Workflow created successfully
```

**Paso 13: Verificar despliegue**

Cada vez que hagas `git push`, Azure desplegará automáticamente.

Ve a GitHub → Actions para ver el progreso.

---

### Fase 5: Probar la API en Azure

#### Paso 14: Obtener la URL
```powershell
az webapp show `
  --resource-group $resourceGroup `
  --name $appName `
  --query defaultHostName `
  --output tsv
```

Verás algo como: `api-clientes.azurewebsites.net`

#### Paso 15: Probar en el navegador
```
https://api-clientes.azurewebsites.net/docs
```

Deberías ver la documentación de FastAPI.

#### Paso 16: Probar endpoints
```powershell
# GET todos los clientes
curl "https://api-clientes.azurewebsites.net/clientes"

# GET documentación
curl "https://api-clientes.azurewebsites.net/docs"

# Health check
curl "https://api-clientes.azurewebsites.net/health"
```

---

## 📊 Resumen de Costos

| Servicio | Tier | Costo Mensual |
|----------|------|--------------|
| App Service | B1 (Basic) | €15-20 |
| Plan de App Service | Incluido | Gratis |
| Storage (si necesario) | Standard | €1-5 |
| **TOTAL** | | **€16-25/mes** |

**Nota:** Los primeros $200 en créditos de Azure son **GRATIS** los primeros 30 días.

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'app'"
**Causa:** requirements.txt no fue instalado
**Solución:** Verificar que `SCM_DO_BUILD_DURING_DEPLOYMENT=true` está configurado

### Error: "Uvicorn not found"
**Causa:** Falta agregar uvicorn a requirements.txt
**Verificar:** Que `requirements.txt` tiene `uvicorn==0.30.6`

### La API tarda mucho en responder
**Causa:** App Service está escalando
**Solución:** Esperar 2-3 minutos. Es normal en el primer inicio.

### No puedo acceder a https://api-clientes.azurewebsites.net
**Causa:** El despliegue aún no terminó
**Solución:** Ejecutar `az webapp log tail` para ver el progreso

---

## 📚 Próximos Pasos (Después de desplegar)

1. **Agregar Base de Datos Real**
   - Azure SQL Database
   - Azure Cosmos DB
   - PostgreSQL flexible server

2. **Agregar Autenticación**
   - Azure AD B2C
   - JWT tokens
   - API Keys

3. **Agregar HTTPS/SSL**
   - Certificado automático (incluido en App Service)

4. **Monitorear Performance**
   - Azure Application Insights
   - Alertas automáticas

5. **CI/CD Pipeline**
   - GitHub Actions automático
   - Pruebas antes de desplegar

---

## ✅ Checklist Rápido

- [ ] Azure CLI instalado y logueado (`az login`)
- [ ] Proyecto listo localmente con tests pasando
- [ ] `.gitignore` creado
- [ ] `Procfile` creado
- [ ] Grupo de recursos creado (`az group create`)
- [ ] Plan de App Service creado
- [ ] Web App creada
- [ ] Startup command configurado
- [ ] Código desplegado (ZIP o GitHub)
- [ ] API accesible en https://api-clientes.azurewebsites.net/docs

---

¿Quieres que proceda con el despliegue? Solo necesito confirmación y podré hacerlo paso a paso.
