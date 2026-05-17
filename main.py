from fastapi import FastAPI
from App.database import Base, engine
from App.routers.contactos import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)