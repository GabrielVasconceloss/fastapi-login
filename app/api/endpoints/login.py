from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud
from app.api import deps


router = APIRouter()

@router.post("/login/")
def login(username: str, password: str, db: Session = Depends(deps.get_db)):
    user = crud.get_user(db, username)
    if user is None or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
