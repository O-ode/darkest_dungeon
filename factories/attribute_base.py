from abc import ABC
from typing import Any

from constants import pretty


class AttributeBase(ABC):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'
