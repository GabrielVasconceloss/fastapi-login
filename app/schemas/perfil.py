from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class PerfilBase(BaseModel):
    CodPerfil: Optional[int] = None
    DescPerfil: Optional[str] = None
    PerfilAdministrador: Optional[str] = None
    DataAtualizacao: Optional[datetime] = None

class Perfil(PerfilBase):
    class Config:
        orm_mode = True
