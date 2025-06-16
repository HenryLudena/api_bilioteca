from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

# URL de database PostgreSQL online (Railway)
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:LaAOsUbAhqLQOUnUJVDSvNAXQNzzDYSX@maglev.proxy.rlwy.net:29447/railway"
# URL de database PostgreSQL local
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/Biblioteca"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Convierte sesión en pydantic model
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
