from pprint import pformat


class EffectModel:
    def __init__(self, description: str):
        self.description: str = description

    def __str__(self):
        return pformat(self.__dict__)

    def __repr__(self):
        return pformat(self.__dict__)
