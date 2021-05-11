
from enum import Enum

class InstType(Enum):
    MARGIN = "MARGIN"
    SPOT = "SPOT"
    SWAP = "SWAP"
    FUTURES = "FUTURES"
    OPTION = "OPTION"