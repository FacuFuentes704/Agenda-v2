from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ContactoCreate(BaseModel):
    nombre: str = Field(min_length=1)
    telefono: str = Field(min_length=1)
    email: EmailStr
    direccion: str = Field(min_length=1)

class ContactoResponse(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str
    direccion: str

class ContactoUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    direccion: Optional[str] = None

    class Config:
        from_attributes = True