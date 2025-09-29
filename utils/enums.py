from enum import Enum, auto


class MaskType(Enum):
    ES = auto()
    MP = auto()

    def __str__(self) -> str:
        return self.name


class FilterType(Enum):
    MPS = "MPS"
    TCSAW = "TC-SAW"
    
    def __str__(self) -> str:
        return self.value
