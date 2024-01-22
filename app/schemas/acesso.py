from typing import Optional
from pydantic import BaseModel

class AcessoBase(BaseModel):
    CodTransacao: Optional[int] = None
    Inclui: Optional[str] = None
    Altera: Optional[str] = None
    Exclui: Optional[str] = None
    Executa: Optional[str] = None

class Acesso(AcessoBase):
    class Config:
        orm_mode = True
