from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import api_router, frontend_router
from .utils import generate_pair

import os

app = FastAPI(
    title="Decypher API",
    description="Decypher task",
    version="v0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router, tags=["API"])
app.include_router(frontend_router, tags=["Frontend"])

if not os.path.exists("public_key.pem"):
    generate_pair()