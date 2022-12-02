from constants import pretty


class OtherInformationModel:
    def __init__(self, items=None):
        self.items: {str: str} = items

    def __repr__(self):
        return pretty(self.__dict__)

    def __str__(self):
        return pretty(self.__dict__)
