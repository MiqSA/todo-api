from src.operations.interface import DataInterface
from src.db.exceptions import NotFoundError
from src.operations.schemas.users import UserIn
from typing import Union, Any

DataObject = dict[str, Any]


def user_exists(data: UserIn, user_interface: DataInterface) -> DataObject:
    try:
        return user_interface.read_by_conditions(conditions={"email": data.email})
    except NotFoundError:
        return None
