from sqlalchemy import Column, Integer, String
from App.database import Base

class Contacto(Base):
    __tablename__ = "Contactos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20))
    email = Column(String(100), nullable=False, unique=True)
    direccion = Column(String(200))