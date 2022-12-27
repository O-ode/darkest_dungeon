from abc import ABC
from typing import Any


class BasicAttribute(ABC):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}:: {type(self.value)}: {self.value}'

    def __eq__(self, other: Any):
        if other is None or type(self) != other.__class__ or self.value != other.value:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.value)


class ResistanceBase(BasicAttribute):
    pass
