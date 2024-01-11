from fastapi import FastAPI
from app.api.api import api_router
from jose import JWTError, jwt

SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"

app = FastAPI(trace_configs=True)

app.include_router(api_router)
