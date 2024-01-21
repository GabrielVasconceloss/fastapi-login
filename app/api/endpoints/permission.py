# from typing import Any, List
# from fastapi import APIRouter, Body, Depends, HTTPException
# from fastapi.encoders import jsonable_encoder
# from pydantic.networks import EmailStr
# from sqlalchemy.orm import Session
#
# from app import crud, models, schemas
# from app.api import deps
#
# router = APIRouter()
#
# @router.get("/permission/", response_model=List[schemas.Permission])
# def read_permission(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_admin),
# ) -> Any:
#     """
#     Retrieve users.
#     """
#     permission = crud.permission.get_multi(db, skip=skip, limit=limit)
#     return permission
#
# @router.post("/permission/", response_model=schemas.Permission)
# def create_permission(
#     *,
#     db: Session = Depends(deps.get_db),
#     permission_in: schemas.PermissionCreate,
#     current_user: models.User = Depends(deps.get_current_active_admin),
# ) -> Any:
#     """
#     Create new Permission.
#     """
#     permission = crud.permission.get_by_permission(db, descr=permission_in.descr)
#     if permission:
#         raise HTTPException(
#             status_code=400,
#             detail="This permission name already exists.",
#         )
#     permission = crud.permission.create(db, obj_in=permission_in)
#
#     return permission
