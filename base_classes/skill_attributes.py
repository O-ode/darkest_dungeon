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
        return f'{self._backwards} backwards, {self._forwards} forwards'


class CritValid(BasicAttribute):
    pass


class Guaranteed(BasicAttribute):
    pass


class StallInvalidating(BasicAttribute):
    pass


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


class Note(BasicAttribute):
    pass


class Dmg(BasicAttribute):
    pass


class DmgMod(BasicAttribute):
    pass


class CritMod(BasicAttribute):
    pass


class Heal(BasicAttribute):
    pass


class TimeCost(BasicAttribute):
    pass
