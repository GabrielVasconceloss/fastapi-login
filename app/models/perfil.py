from sqlalchemy import Column, Integer, String, DateTime, CHAR, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Type
from typing import TYPE_CHECKING

from app.db.base_class import Base

class Perfil(Base):
    __tablename__ = "Perfis"
    CodPerfil = Column(Integer, primary_key=True, index=True)
    DescPerfil = Column(String(50))
    PerfilAdministrador = Column(CHAR(1))
    DataAtualizacao = Column(DateTime, default=datetime.now)
    usuarios = relationship("Usuario", back_populates="perfil")
    acessos = relationship("Acesso", back_populates="perfil", lazy="joined")


