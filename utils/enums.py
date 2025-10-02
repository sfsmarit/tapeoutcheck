from enum import Enum, auto


class DBType(Enum):
    MARIADB = auto()
    SQLITE = auto()


class MaskType(Enum):
    ES = auto()
    MP = auto()

class FETech(Enum):
    MPS = auto()
    TCSAW = auto()
    