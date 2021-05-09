
from enum import Enum

class BillType(Enum):
    # 划转
    TRANSFER = 1
    # 交易
    TRADE = 2
    # 交割
    DELIVERY = 3
    # 强制换币
    FORCE_SWAP = 4
    # 强平
    FORCED_LIQUIDATION = 5
    # ...

class BillSubType(Enum):
    LINEAR = "linear"
    INVERSE = "inverse"
    # ...