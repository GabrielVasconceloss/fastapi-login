from sqlalchemy import Column, Integer, String, CHAR, LargeBinary, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from app.db.base_class import Base
from sqlalchemy.ext import hybrid
from typing import List

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuarios"

    Numero = Column(Integer, primary_key=True, index=True)
    Iniciais = Column(String(10), index=True)
    CodPerfil = Column(Integer, ForeignKey("Perfis.CodPerfil"))
    Nome = Column(String(100))
    Email = Column(String(100))
    Status = Column(CHAR(1))
    Senha = Column(LargeBinary(100))
    IdRecuperaSenha = Column(String(20))
    ResetouSenha = Column(CHAR(1))

    perfil = relationship("Perfil", back_populates="usuarios")

class Perfil(Base):
    __tablename__ = "Perfis"

    CodPerfil = Column(Integer, primary_key=True, index=True)
    DescPerfil = Column(String(50))
    PerfilAdministrador = Column(CHAR(1))
    DataAtualizacao = Column(DateTime, default=datetime.now)

    usuarios = relationship("Usuario", back_populates="perfil")

class Transacao(Base):
    __tablename__ = "Transacoes"

    CodTransacao = Column(Integer, primary_key=True, index=True)
    DescTransacao = Column(String(100))
    TipoTransacao = Column(String(25))
    DataAtualizacao = Column(DateTime, default=datetime.now)

    acessos = relationship("Acesso", back_populates="transacao")

class Acesso(Base):
    __tablename__ = "Acessos"

    CodPerfil = Column(Integer, primary_key=True)
    CodTransacao = Column(Integer, primary_key=True)
    Inclui = Column(String(1))
    Altera = Column(String(1))
    Exclui = Column(String(1))
    Executa = Column(String(1))

    transacao = relationship("Transacao", back_populates="acessos")
    perfil = relationship("Perfil", back_populates="acessos")
