from src.operations.interface import DataInterface, DataObject
from src.db.exceptions import NotFoundError
from src.operations.exceptions import (
    ErrorInCreateUser,
    UniqueValueError,
    UserAlreadyExistError,
)
from src.operations.schemas.users import (
    UserInDB, 
    UserOut,
    UserIn,
)
from src.operations.users import user_exists
from src.security import encode_password, create_hash_id
from typing import Callable, Any


def user_serializer(
        model: UserInDB,
        data: UserIn,
        hasher_maker: Callable[[], str] = create_hash_id,
        encoder: Callable[[], str] = encode_password,
    ) -> UserInDB:
    return model(
            hashed_id=hasher_maker(),
            username=data.username,
            email=data.email,
            hashed_password=encoder(data.password),
        )

def user_signup(
        data: UserIn,
        user_interface: DataInterface,
        user_serializer: Callable[[Any], UserInDB]=user_serializer) -> UserOut:
    try:
        user = user_exists(data=data, user_interface=user_interface)
        if user is not None:
            raise UserAlreadyExistError("User already exists.")

        user_data = user_serializer(model=UserInDB, data=data)
        res = user_interface.create(data=user_data.model_dump())
        return UserOut(email=res["email"])
    except UserAlreadyExistError:
        raise 
    except ValueError as err:
        raise UniqueValueError("Username already exists.", err)
    except Exception as err:
        raise ErrorInCreateUser("Error in create user", err)
