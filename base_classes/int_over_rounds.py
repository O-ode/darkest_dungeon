from abc import ABC


class IntOverRounds(ABC):
    def __init__(self, int_value: int, n_rounds: int):
        self.int_value = int_value
        self.n_rounds = n_rounds

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.int_value} over {self.n_rounds} rounds'
