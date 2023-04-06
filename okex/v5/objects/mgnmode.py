
from enum import Enum
from typing import TypeAlias, Union

# 仓位类型
class MgnMode(Enum):
    # 保证金模式
    ISOLATED = "isolated"
    CROSS = "cross"
    # 非保证金模式
    CASH = "cash"

MgnModeT: TypeAlias = Union[MgnMode, str]