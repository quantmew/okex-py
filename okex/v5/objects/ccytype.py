
from enum import Enum
from typing import TypeAlias, Union

class CcyType(Enum):
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
    ADA = "ADA"
    TRX = "TRX"
    OKB = "OKB"
    UNI = "UNI"
    # ...

    def __str__(self) -> str:
        return self.value

CcyTypeT: TypeAlias = Union[CcyType, str]