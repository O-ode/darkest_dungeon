from abc import ABC
from typing import Any


class BasicAttribute(ABC):
    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


class Crit(BasicAttribute):
    pass


class HP(BasicAttribute):
    pass


class Dodge(BasicAttribute):
    pass


class Prot(BasicAttribute):
    pass


class Spd(BasicAttribute):
    pass


class SkillName(BasicAttribute):
    pass


class Rank(BasicAttribute):
    pass


class Target(BasicAttribute):
    pass


class Effect(BasicAttribute):
    pass


class Range(BasicAttribute):
    pass


class Accuracy(BasicAttribute):
    pass


class Limit(BasicAttribute):
    pass


class AccMod(BasicAttribute):
    pass


class Movement(BasicAttribute):
    pass


class CritBuffBonus(BasicAttribute):
    pass


class Religious(BasicAttribute):
    pass


class Provisions(BasicAttribute):
    pass


class ResistanceBase(BasicAttribute):
    pass


class Stun(ResistanceBase):
    pass


class Move(ResistanceBase):
    pass


class Blight(ResistanceBase):
    pass


class Bleed(ResistanceBase):
    pass


class Disease(ResistanceBase):
    pass


class Debuff(ResistanceBase):
    pass


class DeathBlow(ResistanceBase):
    pass


class Trap(ResistanceBase):
    pass


class ResolveLevel(BasicAttribute):
    pass


class Note(BasicAttribute):
    pass


class Dmg(BasicAttribute):
    pass


class IntRange(ABC):

    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.upper}-{self.lower}'


class DmgRange(IntRange):
    pass


class IntOverRounds(ABC):
    def __init__(self, int_value: int, n_rounds: int):
        self.int_value = int_value
        self.n_rounds = n_rounds

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.int_value} over {self.n_rounds} rounds'
