from fastapi import Request
from src.logger import Log
import time
from uuid import uuid4

ORIGINS = [
    "http://localhost",
]
CORS_MIDDLEWARE = {
    "allow_origins": ORIGINS,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

logf = Log().main(__name__)


async def log_middleware(request: Request, call_next) -> dict:
    request.state.request_id = str(uuid4())
    
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start

    
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time,
        'request_id': request.state.request_id,
    }
    logf.info(log_dict)
    return response
