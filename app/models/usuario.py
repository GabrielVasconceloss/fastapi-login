from sqlalchemy import Column, Integer, String, CHAR, LargeBinary, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import hybrid
from typing import List
from typing import TYPE_CHECKING
from app.db.base_class import Base

if TYPE_CHECKING:
    from .perfil import Perfil  # noqa: F401
    from .acesso import Acesso  # noqa: F401

class Usuario(Base):
    __tablename__ = "Usuarios"

    Numero = Column(Integer, primary_key=True, index=True)
    Iniciais = Column(String(10), index=True)
    CodPerfil = Column(Integer, ForeignKey("Perfis.CodPerfil"))
    Nome = Column(String(100))
    Email = Column(String(100))
    Status = Column(CHAR(1))
    Senha = Column(String(200))
    IdRecuperaSenha = Column(String(20))
    ResetouSenha = Column(CHAR(1))

    perfil = relationship("Perfil", back_populates="usuarios")

