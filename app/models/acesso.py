from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .perfil import Perfil  # noqa: F401
    from .transacao import Transacao
    from .usuario import Usuario

class Acesso(Base):
    __tablename__ = "Acessos"

    CodPerfil = Column(Integer, ForeignKey("Perfis.CodPerfil"), primary_key=True)
    CodTransacao = Column(Integer, ForeignKey("Transacoes.CodTransacao"), primary_key=True)
    Inclui = Column(CHAR(1))
    Altera = Column(CHAR(1))
    Exclui = Column(CHAR(1))
    Executa = Column(CHAR(1))
    perfil = relationship("Perfil", back_populates="acessos")
    transacao = relationship("Transacao", back_populates="acessos")


