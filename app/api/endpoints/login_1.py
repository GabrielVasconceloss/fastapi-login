# from datetime import timedelta
# from typing import Any
from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
#from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.usuario import Usuario
from app import schemas, models

router = APIRouter()
@router.get("/users/", response_model=List[schemas.usuario.Usuario])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db)):
    users = db.query(Usuario).offset(skip).limit(limit).all()
    return users