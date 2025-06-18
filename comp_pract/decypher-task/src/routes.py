from fastapi import APIRouter, Form, Request, status
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

from typing import Annotated

from .utils import decrypt, generate_pair, encrypt_message

import base64


api_router = APIRouter()
frontend_router = APIRouter()

templates = Jinja2Templates(directory="templates")

# API routes

@api_router.get("/login")
async def author():
    return {"author": "1149920"}


@api_router.post("/decypher")
async def login(
    key: Annotated[str, Form()], 
    secret: Annotated[str, Form()]
):
    try:
        key_bin = base64.b64decode(key)
        secret_bin = base64.b64decode(secret)
        decrypted = decrypt(key_bin, secret_bin)
        return {"result": decrypted}
    except:
        raise(HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Decryption failed! Wrong key?"))


@api_router.get("/encrypt/{secret}")
async def encrypt(secret: str):
    try:
        key, encrypted_message = encrypt_message(secret)
        return {"key": base64.b64encode(key).decode("utf-8"), "secret": base64.b64encode(encrypted_message)}
    except:
        raise(HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Encryption failed! RSA key missing?"))


# Frontend routes

@frontend_router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})