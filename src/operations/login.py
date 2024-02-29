from src.security import create_access_token,create_refresh_token, check_password
from src.operations.schemas.users import UserIn, TokenOut, TokenCreate
from src.operations.interface import DataInterface
from src.operations.users import user_exists
from src.operations.exceptions import EmailIncorrectError, PasswordIncorrectError
from typing import Any
from datetime import datetime

DataObject = dict[str, Any]


def login(data: UserIn, user_interface: DataInterface, token_interface: DataInterface) -> TokenOut:
    user = user_exists(data=data, user_interface=user_interface)


    if user is None:
        raise EmailIncorrectError()
    if not check_password(data.password, user["hashed_password"]):
        raise PasswordIncorrectError()
    
    access = create_access_token(user["hashed_id"])
    refresh = create_refresh_token(user["hashed_id"])

    token = TokenCreate(
        user_id=user["hashed_id"],
        access_token=access,
        refresh_token=refresh,
        status=True,
        created_date=datetime.now(),
    )
    res = token_interface.create(data=token.model_dump())
    return TokenOut(
        access_token=res["access_token"],
        refresh_token=res["refresh_token"])

