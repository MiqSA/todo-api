from fastapi import APIRouter, Depends, Request
from src.auth_bearer import jwt_bearer
from src.logger import log_http_expections
from typing import Any
from src.operations.todo import read_todos


router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
@log_http_expections
async def read_root(request: Request, limit: int = 5, _: str = Depends(jwt_bearer)) -> list[Any]:
    return await read_todos(request=request, limit=limit)