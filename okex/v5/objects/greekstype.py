
from enum import Enum
from typing import TypeAlias, Union

class GreeksType(Enum):
    PA = "PA"
    BS = "BS"

GreeksTypeT: TypeAlias = Union[GreeksType, str]