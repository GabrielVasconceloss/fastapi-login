from sqlalchemy.orm import Session
from app.models import user

def get_user(db: Session, username: str):
    return db.query(user.User).filter(user.User.username == username).first()
