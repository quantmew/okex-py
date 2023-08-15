
from enum import Enum
from typing import TypeAlias, Union

class GreeksType(Enum):
    PA = "PA"
    BS = "BS"

    def __str__(self) -> str:
        return self.value

GreeksTypeT: TypeAlias = Union[GreeksType, str]