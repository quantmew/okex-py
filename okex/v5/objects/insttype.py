
from enum import Enum
from typing import TypeAlias, Union

class InstType(Enum):
    MARGIN = "MARGIN"
    SPOT = "SPOT"
    SWAP = "SWAP"
    FUTURES = "FUTURES"
    OPTION = "OPTION"
    ANY = "ANY"

InstTypeT: TypeAlias = Union[InstType, str]