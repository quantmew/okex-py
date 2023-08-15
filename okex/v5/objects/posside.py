from enum import Enum

class PosSide(Enum):
    LONG = "long"
    SHORT = "short"
    NET = 'net'

    def __str__(self) -> str:
        return self.value