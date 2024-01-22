from typing import Optional, List
from .perfil import PerfilBase
from .acesso import AcessoBase
from pydantic import BaseModel, EmailStr


# Shared properties
class UsuarioBase(BaseModel):
    Iniciais: Optional[str] = None
    Nome: Optional[str] = None
    Email: Optional[str] = None
    Status: Optional[str] = None
    Senha: Optional[str] = None
    IdRecuperaSenha: Optional[str] = None
    ResetouSenha: Optional[str] = None

# Properties to receive via API on creation
class UsuarioCreate(UsuarioBase):
    Email: EmailStr
    Senha: str


# Properties to receive via API on update
class UsuarioUpdate(UsuarioBase):
    Senha: Optional[str] = None
    CodPerfil: Optional[int] = 1


class UsuarioInDBBase(UsuarioBase):
    Numero: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Usuario(UsuarioInDBBase):
    CodPerfil: Optional[int] = None
    perfil: Optional[PerfilBase] = None
    acessos: Optional[List[AcessoBase]] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB
class UsuarioInDB(UsuarioInDBBase):
    Senha: str


class UsuarioBaseUpdate(BaseModel):
    Iniciais: Optional[str] = None
    CodPerfil: Optional[int] = 1
    Nome: Optional[str] = None
    Email: Optional[str] = None
    Status: Optional[str] = None
    Senha: Optional[str] = None