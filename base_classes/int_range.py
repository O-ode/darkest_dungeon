from abc import ABC


class IntRange(ABC):

    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.lower}-{self.upper}'


class DmgRange(IntRange):
    pass
