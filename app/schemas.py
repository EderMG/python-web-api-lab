"""Esquemas de validación para requests y responses."""
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ClienteBase(BaseModel):
    """Atributos comunes de un cliente."""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre completo del cliente")
    email: EmailStr = Field(..., description="Email válido del cliente")
    edad: int = Field(..., ge=18, le=120, description="Edad del cliente (18-120)")
    activo: bool = Field(default=True, description="Si el cliente está activo")


class ClienteCrear(ClienteBase):
    """Schema para crear un nuevo cliente."""
    pass


class ClienteActualizar(BaseModel):
    """Schema para actualizar un cliente (todos los campos son opcionales)."""
    nombre: str | None = Field(None, min_length=1, max_length=100)
    email: EmailStr | None = Field(None)
    edad: int | None = Field(None, ge=18, le=120)
    activo: bool | None = None


class ClienteRespuesta(ClienteBase):
    """Schema para la respuesta de un cliente."""
    id: int = Field(..., description="ID único del cliente")
    
    model_config = ConfigDict(from_attributes=True)
