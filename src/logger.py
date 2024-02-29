from dataclasses import dataclass
from fastapi import HTTPException
from functools import wraps
import logging
import os
from string import Template
import sys
from typing import Callable, Any


FORMAT = '%(asctime)s %(levelname)s %(name)s %(message)s'
DEFAULT_ERROR_MESSAGE = "Error! Bad request!"
DEFAULT_ERROR_STATUS_CODE = 400


@dataclass
class Log:
    path: str = 'logs/'
    file: str = 'todo_api.log'
    level: int = logging.INFO

    def create_path(self) -> None:
        if not os.path.exists(self.path):
            os.mkdir(f'{self.path}')

    def format_log(self) -> None:
        logging.basicConfig(
            filename=f'{self.path}{self.file}',
            level=self.level,
            format=FORMAT,
        )

    def main(self, name: str) -> logging.Logger:
        try:
            self.create_path()
            self.format_log()
            return logging.getLogger(name)
        except Exception:
            raise

def new_logger_expection(
    exc: Exception,
    func: Callable[[Any], Any],
    request_id: str, 
    loggerf: Callable[[str], logging.Logger] = Log().main
    ) -> None:
    logger = loggerf(sys.modules[func.__module__].__name__)
    msg = Template(
        'Error in $func_name'
        ).substitute(func_name=func.__name__)
    log_dict = {
        'request_id': request_id,
        'error': msg,
    }
    logger.exception(log_dict, exc_info=exc)


def log_http_expections(func):
    """ An exception solver decorator. This function catches the exception,
    logs, and raises an appropriate HTTP exception. """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request_id = kwargs['request'].state.request_id
        try: 
            res = await func(*args, **kwargs)
            return res
        except HTTPException as err_http:
            new_logger_expection(exc=err_http, func=func, request_id=request_id)
            raise
        except Exception as err:
            new_logger_expection(exc=err, func=func, request_id=request_id)
            raise HTTPException(
                status_code=DEFAULT_ERROR_STATUS_CODE,
                detail= {
                    "error": {
                        "reason": str(err),
                    }
                }
            )
    return wrapper
