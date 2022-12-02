from constants import pretty


class EffectModel:
    def __init__(self, description: str):
        self.description: str = description

    def __str__(self):
        return pretty(self.__dict__)

    def __repr__(self):
        return pretty(self.__dict__)
