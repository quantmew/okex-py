
from enum import Enum

class CtType(Enum):
    LINEAR = "linear"
    INVERSE = "inverse"

    def __str__(self) -> str:
        return self.value