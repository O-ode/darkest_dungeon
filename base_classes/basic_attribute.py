from abc import ABC
from typing import Any


class BasicAttribute(ABC):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


class ResistanceBase(BasicAttribute):
    pass


class OtherAttributeBase(BasicAttribute):
    pass
