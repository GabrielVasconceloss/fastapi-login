from sqlalchemy import Column, Integer, String, Sequence, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    descr = Column(String(50), unique=True, index=True)

    users = relationship('User', back_populates='permission')