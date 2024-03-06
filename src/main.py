from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from .db.engine import init_db
from .middlewares import CORS_MIDDLEWARE, log_middleware
from .routers.v1 import (
    health,
    login,
    signup,
    todo,
)
from .settings import DB_URL
from .version import VERSION
from .logger import Log


logf = Log().main(__name__)


async def startup_event():
    init_db(DB_URL)
    logf.info("API started with success!")


async def shutdown_event():
    logf.info("API stopped...")

app = FastAPI(
    title="TODO API",
    description="A API to get random TODOs",
    version=VERSION,
    docs_url="/docs",
    redoc_url=None,
    on_startup=[startup_event],
    on_shutdown=[shutdown_event],
)

# Middlewares
app.add_middleware(CORSMiddleware, **CORS_MIDDLEWARE)
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

# Routes
app.include_router(health.router, prefix="/v1")
app.include_router(login.router, prefix="/v1")
app.include_router(signup.router, prefix="/v1")
app.include_router(todo.router, prefix="/v1")
