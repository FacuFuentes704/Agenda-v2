from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models import Contacto
from App.schemas import ContactoCreate, ContactoResponse
from sqlalchemy import func

router = APIRouter(
    prefix="/contactos",
    tags=["contactos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ContactoResponse])
def listar_contactos(db: Session = Depends(get_db)):
    contactos = db.query(Contacto).all()
    return contactos

@router.post("/", response_model=ContactoResponse)
def crear_contacto(contacto: ContactoCreate, db: Session = Depends(get_db)):
    nuevo_contacto = Contacto(nombre = contacto.nombre, telefono = contacto.telefono, email = contacto.email, direccion = contacto.direccion)
    db.add(nuevo_contacto)
    db.commit()
    db.refresh(nuevo_contacto)
    return nuevo_contacto

@router.get("/buscar", response_model=list[ContactoResponse])
def buscar_nombre(nombre: str, db: Session = Depends(get_db)):
    respuesta = db.query(Contacto).filter(func.lower(Contacto.nombre) == func.lower(nombre)).all()
    if not respuesta:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    else:
        return respuesta
        
@router.delete("/{id}", status_code=204)
def eliminar_contacto(id: int, db: Session = Depends(get_db)):
    resultado = db.query(Contacto).filter(Contacto.id == id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    else:
        db.delete(resultado)
        db.commit()
 