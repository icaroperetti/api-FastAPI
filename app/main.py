from fastapi import FastAPI
from .routes import health_check, persons, persons_address
from dotenv import load_dotenv
import os
from app.config.db import Database

load_dotenv()

app = FastAPI()

app.include_router(health_check.router)
app.include_router(persons.router)
app.include_router(persons_address.router)
