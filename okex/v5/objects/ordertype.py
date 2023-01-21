from enum import Enum

class OrderType(Enum):
    # 市价单
    MARKET = "market"
    # 限价单
    LIMIT = "limit"
    # 只做maker单
    POST_ONLY = "post_only"
    # 全部成交或立即取消
    FOK = "fok"
    # 立即成交并取消剩余
    IOC = "ioc"