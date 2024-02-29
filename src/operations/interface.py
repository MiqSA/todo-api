from typing import Any, Protocol


DataObject = dict[str, Any]

class DataInterface(Protocol):
    def read_by_conditions(self, conditions: DataObject) -> DataObject:
        ...
    
    def create(self, data: DataObject) -> DataObject:
        ...

