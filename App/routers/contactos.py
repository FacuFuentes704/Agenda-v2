from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models import Contacto
from App.schemas import ContactoCreate, ContactoResponse

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
