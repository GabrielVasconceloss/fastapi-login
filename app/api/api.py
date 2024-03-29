from fastapi import APIRouter
from app.api.endpoints import login, user, permission


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, tags=["user"])
api_router.include_router(permission.router, tags=["permission"])
