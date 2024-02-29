import httpx
from typing import Any
from src.settings import API_URL
from .exceptions import ErrorTodosAPI


def fetch_todos(url: str = API_URL) -> dict[str, Any]:
    try:
        response = httpx.get(url)
        result = {
            'status_code': response.status_code,
            'data_raw': [],
        }
        if response.status_code == 200:
            result['data_raw'] = response.json()
        return result
    except Exception as err:
        raise ErrorTodosAPI("Error in get todos", err)
