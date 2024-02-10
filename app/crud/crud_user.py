from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session, joinedload
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.usuario import Usuario
from app.models.acesso import Acesso
from app.models.perfil import Perfil
from app.models.permission import Permission
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioBaseUpdate
from app.schemas.permission import PermissionCreate


class CRUDUsuario(CRUDBase[Usuario, UsuarioCreate, UsuarioBaseUpdate]):
    def get_by_email(self, db: Session, *, Email: str) -> Optional[Usuario]:
        return db.query(Usuario).filter(Usuario.Email == Email).first()

    def get_by_acess(self, db: Session, *, CodPerfil: int, CodTransacao: int) -> Optional[Acesso]:
        return db.query(Acesso).filter(Acesso.CodPerfil == CodPerfil, Acesso.CodTransacao == CodTransacao).first()

    def get_detail_user(self, db: Session, *, Numero: int) -> Any:
        user = (
            db.query(Usuario)
            .filter(Usuario.Numero == Numero)
            .options(
                joinedload(Usuario.perfil)
            )
            .first()
        )
        return user

    def get_user_accesses(self, db: Session, *, user: Usuario) -> Any:
        accesses = db.query(Acesso).filter(Acesso.CodPerfil == user.CodPerfil).all()
        return accesses


    def create(self, db: Session, *, obj_in: UsuarioCreate) -> Usuario:
        db_obj = Usuario(
            Email=obj_in.Email,
            Senha=get_password_hash(obj_in.Senha),
            Iniciais=obj_in.Iniciais,
            CodPerfil=obj_in.CodPerfil,
            Nome=obj_in.Nome,
            Status=obj_in.Status,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Usuario, obj_in: Union[UsuarioBaseUpdate, Dict[str, Any]]
    ) -> Usuario:

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "Senha" in update_data and update_data["Senha"]:
            hashed_password = get_password_hash(update_data["Senha"])
            del update_data["Senha"]
            update_data["Senha"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, Email: str, password: str) -> Optional[Usuario]:
        Usuario = self.get_by_email(db, Email=Email)
        if not Usuario:
            return None
        if not verify_password(password, Usuario.Senha):
            return None
        return Usuario

    def is_active(self, Usuario: Usuario) -> bool:
        return Usuario.Status == 'A'

    def is_admin(self, Usuario: Usuario) -> bool:
        return Usuario.CodPerfil == 1



# def get_Usuario(db: Session, Usuarioname: str):
#     return db.query(Usuario.Usuario).filter(Usuario.Usuario.Usuarioname == Usuarioname).first()

usuario = CRUDUsuario(Usuario)