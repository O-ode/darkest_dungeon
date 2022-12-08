from abc import ABC
from typing import Any


class BasicAttribute(ABC):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


class IntRange(ABC):

    def __init__(self, upper: int, lower: int):
        self.upper = upper
        self.lower = lower

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.upper}-{self.lower}'


class IntOverRounds(ABC):
    def __init__(self, int_value: int, n_rounds: int):
        self.int_value = int_value
        self.n_rounds = n_rounds

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.int_value} over {self.n_rounds} rounds'
