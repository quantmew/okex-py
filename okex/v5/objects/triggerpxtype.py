
from enum import Enum

class TriggerPxType(Enum):
    # 最新价格
    LAST = "last"
    # 指数价格
    INDEX = "index"
    # 标记价格
    MARK = "mark"

    def __str__(self) -> str:
        return self.value