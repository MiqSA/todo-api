from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.db.models.settings import Base, to_dict
from typing import Any
from src.db.exceptions import NotFoundError


DataObject = dict[str, Any]

class DBInterface:
    def __init__(self, base: Base, session_db: Session) -> None:
        self.db_class = base
        self.db = session_db
    
    def read_by_conditions(self, conditions: DataObject) -> DataObject:
        data = self.db.query(self.db_class).filter_by(**conditions).first()
        if data is None:
            raise NotFoundError("Data not found")
        return to_dict(data)

    def create(self, data: DataObject) -> DataObject:
        try:
            item: Base = self.db_class(**data)
            self.db.add(item)
            self.db.commit()
            result = to_dict(item)
            return result
        except IntegrityError as err:
            self.db.rollback()
            raise ValueError(err)

