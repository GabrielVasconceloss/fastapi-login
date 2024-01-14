from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.permission import Permission
from app.schemas.permission import PermissionCreate, PermissionUpdate


class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):

    def get_by_permission(self, db: Session, *, descr: str) -> Optional[Permission]:
        return db.query(Permission).filter(Permission.descr == descr).first()

    def create(self, db: Session, *, obj_in: PermissionCreate) -> Permission:
        db_obj = Permission(descr=obj_in.descr)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(Permission).offset(skip).limit(limit).all()


    # def update(
    #     self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> User:
    #
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if "password" in update_data and update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
    #     user = self.get_by_email(db, email=email)
    #     if not user:
    #         return None
    #     if not verify_password(password, user.password):
    #         return None
    #     return user

    # def is_active(self, user: User) -> bool:
    #     return user.is_active
    #
    # def is_admin(self, user: User) -> bool:
    #     return user.email == 'admin@admin.com'


permission = CRUDPermission(Permission)