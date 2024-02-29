from fastapi import APIRouter, HTTPException, Depends, Request
from src.operations.login import (
    EmailIncorrectError,
    login,
    PasswordIncorrectError,
)
from src.operations.schemas.users import Login, TokenOut
from src.db.db_interface import DBInterface
from src.db.models.user import DBUser, DBToken
from src.db.engine import get_db, Session
from src.logger import log_http_expections


router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
@log_http_expections
async def api_user_signup(
    data: Login,
    request: Request,
    db: Session = Depends(get_db),
    ) -> TokenOut:
    try:
        user_interface = DBInterface(base=DBUser, session_db=db)
        token_interface = DBInterface(base=DBToken, session_db=db)
        return login(
            data=data,
            user_interface=user_interface,
            token_interface=token_interface,
        )
    except EmailIncorrectError:
        raise HTTPException(
            status_code=400,
            detail="Email incorrect!")
    except PasswordIncorrectError:
        raise HTTPException(
            status_code=400,
            detail="Password incorrect!")
