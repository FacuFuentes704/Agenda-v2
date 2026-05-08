from fastapi import FastAPI
from App.database import Base, engine
from App.routers.contactos import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)