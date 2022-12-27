from base_classes.basic_attribute import BasicAttribute


class Level(BasicAttribute):
    pass


class Launch(BasicAttribute):
    pass


class Move:
    def __init__(self, backwards: int, forwards: int):
        self._backwards = backwards
        self._forwards = forwards

    def __repr__(self):
        return f'{self.__class__.__name__}:: {self._backwards} backwards, {self._forwards} forwards'


class Heal:
    def __init__(self, lower: int, upper: int):
        self._lower = lower
        self._upper = upper

    def __repr__(self):
        return f'{self.__class__.__name__}:: {self._lower}-{self._upper} hp'


class Target(BasicAttribute):
    pass


class Effect(BasicAttribute):
    pass


class SkillType(BasicAttribute):
    pass


class Accuracy(BasicAttribute):
    pass


class Limit(BasicAttribute):
    pass


class DmgMod(BasicAttribute):
    pass


class CritMod(BasicAttribute):
    pass


class TimeCost(BasicAttribute):
    pass
