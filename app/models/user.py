from sqlalchemy import Column, Integer, String, Sequence, Boolean
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(255))
    is_active = Column(Boolean(), default=True, server_default="1")
    fullname = Column(String(255), nullable=True, index=True)
    email = Column(String(255), index=True, unique=True)
    telephone = Column(String(20))

    menu = Column(Boolean(), default=True, server_default="1")