from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
            if not SQLALCHEMY_DATABASE_URL:
                raise ValueError("DATABASE_URL is not set in the environment variables")

            cls._instance.engine = create_engine(SQLALCHEMY_DATABASE_URL)
            cls._instance.SessionLocal = scoped_session(
                sessionmaker(
                    autocommit=False, autoflush=False, bind=cls._instance.engine
                )
            )
        return cls._instance


def get_db():
    db = Database().SessionLocal()
    try:
        yield db
    finally:
        db.close()
