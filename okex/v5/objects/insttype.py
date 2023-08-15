
from enum import Enum
from typing import TypeAlias, Union

class InstType(Enum):
    MARGIN = "MARGIN"
    SPOT = "SPOT"
    SWAP = "SWAP"
    FUTURES = "FUTURES"
    OPTION = "OPTION"
    ANY = "ANY"

    def __str__(self) -> str:
        return self.value

InstTypeT: TypeAlias = Union[InstType, str]