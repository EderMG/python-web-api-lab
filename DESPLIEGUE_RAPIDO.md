# ⚡ DESPLIEGUE RÁPIDO EN AZURE (5 MINUTOS)

## Prerequisitos checklist
- [ ] Cuenta de Azure (https://azure.microsoft.com/)
- [ ] Azure CLI instalado
- [ ] Logueado en Azure (`az login`)

---

## COPIAR Y EJECUTAR ESTOS COMANDOS

### Paso 1: Define variables
```powershell
$appName = "api-clientes"
$resourceGroup = "$appName-rg"
$appPlan = "$appName-plan"
$region = "eastus"
```

### Paso 2: Crear recursos en Azure
```powershell
# Crear grupo de recursos
az group create --name $resourceGroup --location $region

# Crear plan App Service
az appservice plan create `
  --name $appPlan `
  --resource-group $resourceGroup `
  --sku B1 `
  --is-linux

# Crear Web App
az webapp create `
  --resource-group $resourceGroup `
  --plan $appPlan `
  --name $appName `
  --runtime "PYTHON:3.12"
```

### Paso 3: Configurar startup
```powershell
# Comando para iniciar FastAPI
az webapp config set `
  --resource-group $resourceGroup `
  --name $appName `
  --startup-file "python -m uvicorn app.main:app --host 0.0.0.0"

# Habilitar build automático
az webapp config appsettings set `
  --resource-group $resourceGroup `
  --name $appName `
  --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

### Paso 4: Crear Procfile (ejecutar en folder del proyecto)
```powershell
Add-Content -Path Procfile -Value "web: uvicorn app.main:app --host 0.0.0.0 --port 8000"
```

### Paso 5: Desplegar desde ZIP
```powershell
# En la carpeta del proyecto
Compress-Archive -Path app, tests, requirements.txt, conftest.py, Procfile `
  -DestinationPath deploy.zip

# Desplegar
az webapp deployment source config-zip `
  --resource-group $resourceGroup `
  --name $appName `
  --src deploy.zip

# Ver logs en tiempo real
az webapp log tail `
  --resource-group $resourceGroup `
  --name $appName
```

### Paso 6: Probar
```powershell
# Obtener URL
az webapp show `
  --resource-group $resourceGroup `
  --name $appName `
  --query defaultHostName

# Abrir en navegador:
# https://api-clientes.azurewebsites.net/docs
```

---

## 🎉 ¡Listo!

Deberías ver tu API en:
```
https://api-clientes.azurewebsites.net/docs
```

---

## Si algo falla

```powershell
# Ver logs del despliegue
az webapp log tail --resource-group $resourceGroup --name $appName

# Revisar configuración
az webapp config show --resource-group $resourceGroup --name $appName

# Verificar que está ejecutándose
curl "https://$appName.azurewebsites.net/health"
```

---

## Limpiar recursos (cuando termines)
```powershell
# Eliminar todo (cuidado, esto borra el recurso)
az group delete --name $resourceGroup --yes
```

Este comando elimina la Web App, el plan y el grupo de recursos. **Esto reduce costos a $0/mes**.
