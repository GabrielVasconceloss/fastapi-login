from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Usuario])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.Usuario = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.usuario.get_multi(db, skip=skip, limit=limit)
    return users



@router.get("/me", response_model=schemas.Usuario)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.Usuario = Depends(deps.get_current_active_user),
) -> Any:

    """
    Get current user.
    """
    user = crud.usuario.get_detail_user(db, Numero=current_user.Numero)
    print(user)
    return user



@router.put("/me", response_model=schemas.Usuario)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    Iniciais: str = Body(None),
    CodPerfil: int = Body(None),
    Nome: str = Body(None),
    Email: EmailStr = Body(None),
    Status: str = Body(None),
    Senha: str = Body(None),
    current_user: models.Usuario = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UsuarioUpdate(**current_user_data)
    if Iniciais is not None:
        user_in.Iniciais = Iniciais
    if CodPerfil is not None:
        user_in.CodPerfil = CodPerfil
    if Nome is not None:
        user_in.Nome = Nome
    if Email is not None:
        user_in.Email = Email
    if Status is not None:
        user_in.Status = Status
    if Senha is not None:
        user_in.Senha = Senha
    user = crud.usuario.update(db, db_obj=current_user, obj_in=user_in)
    return user








@router.get("/{user_id}", response_model=schemas.Usuario)
def read_user_by_id(
    user_id: int,
    current_user: models.Usuario = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.usuario.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.usuario.is_admin(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    return user




@router.post("/", response_model=schemas.Usuario)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UsuarioCreate,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new user.
    """
    user = crud.usuario.get_by_email(db, Email=user_in.Email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.usuario.create(db, obj_in=user_in)
    # if settings.EMAILS_ENABLED and user_in.email:
    #     send_new_account_email(
    #         email_to=user_in.email, username=user_in.email, password=user_in.password
    #     )
    return user

@router.put("/{user_id}", response_model=schemas.Usuario)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UsuarioBaseUpdate,
    current_user: models.Usuario = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a user.
    """
    user = crud.usuario.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.usuario.update(db, db_obj=user, obj_in=user_in)
    return user





