from fastapi import FastAPI
from .routes import health_check, persons
from dotenv import load_dotenv
import os
from app.config.db import Database

load_dotenv()

db_instance = Database()

try:
    with db_instance.engine.connect() as connection:
        print("Conexão bem-sucedida!")
except Exception as e:
    raise ValueError(f"Conexão falhou: {e}")


app = FastAPI()

app.include_router(health_check.router)
app.include_router(persons.router)
