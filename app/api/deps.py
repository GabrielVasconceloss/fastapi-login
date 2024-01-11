from fastapi import Depends
from sqlalchemy.orm import Session
from app import crud
from app.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
