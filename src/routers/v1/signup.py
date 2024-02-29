from fastapi import APIRouter, HTTPException, Depends, Request
from src.operations.signup import (
    ErrorInCreateUser,
    user_signup,
    UniqueValueError,
    UserAlreadyExistError,
)
from src.operations.schemas.users import UserIn, UserOut
from src.db.db_interface import DBInterface
from src.db.models.user import DBUser
from src.db.engine import get_db, Session
from src.logger import log_http_expections


router = APIRouter(
    prefix="/signup",
    tags=["signup"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
@log_http_expections
async def api_user_signup(
    data: UserIn,
    request: Request,
    db: Session = Depends(get_db),
    ) -> UserOut:
    try:
        interface = DBInterface(base=DBUser, session_db=db)
        return user_signup(
            user_interface=interface,
            data=data,
        )
    except ErrorInCreateUser:
        raise HTTPException(
            status_code=400,
            detail="Error in signup")
    except UserAlreadyExistError:
        raise HTTPException(
            status_code=400,
            detail="User already exist.")
    except UniqueValueError:
        raise HTTPException(
            status_code=422,
            detail="This username is not available, try another!")
