from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import Optional
from datetime import datetime
from typing import TYPE_CHECKING

class Transacao(Base):
    __tablename__ = "Transacoes"

    CodTransacao = Column(Integer, primary_key=True, index=True)
    DescTransacao = Column(String(100))
    TipoTransacao = Column(String(25))
    DataAtualizacao = Column(DateTime, default=datetime.now)

    acessos = relationship("Acesso", back_populates="transacao")