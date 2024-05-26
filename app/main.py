from fastapi import FastAPI
from .routes import health_check

app = FastAPI()


app.include_router(health_check.router)
