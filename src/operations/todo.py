from fastapi import Request
from src.logger import Log
from services.todo.main import fetch_todos
from typing import Any, Callable
from .exceptions import DataNotFound, FieldNotSupportedError


logf = Log().main(__name__)


def data_filtered(data: dict[str, Any], limit: int):
    data["data_raw"] = [{"id": i["id"], "title": i["title"]} for i in data["data_raw"][:limit]]
    return data["data_raw"]

def data_logger(data: dict[str, Any], request= Request):
    data["request_id"] = request.state.request_id
    logf.info(data)

async def read_todos(
        request: Request,
        limit: int,
        fetch: Callable[[], Any] = fetch_todos
    ) -> list[Any]:
    try:
        result = fetch()
        if not isinstance(result, dict):
            raise DataNotFound()
    
        data_logger(data=result, request=request)
        return data_filtered(data=result, limit=limit)
    except KeyError as err:
        raise FieldNotSupportedError(err)
