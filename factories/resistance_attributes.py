from abc import ABC

from constants import pretty
from factories.attribute_base import BasicAttribute
from selenium_local.text_modifying_functions import text_to_float_div_100


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


class ResistancesFactory(ABC):

    @classmethod
    def get_stun(cls, value: str) -> Stun:
        return Stun(text_to_float_div_100(value))

    @classmethod
    def get_move(cls, value: str) -> Move:
        return Move(text_to_float_div_100(value))

    @classmethod
    def get_blight(cls, value: str) -> Blight:
        return Blight(text_to_float_div_100(value))

    @classmethod
    def get_bleed(cls, value: str) -> Bleed:
        return Bleed(text_to_float_div_100(value))

    @classmethod
    def get_disease(cls, value: str) -> Disease:
        return Disease(text_to_float_div_100(value))

    @classmethod
    def get_debuff(cls, value: str) -> Debuff:
        return Debuff(text_to_float_div_100(value))

    @classmethod
    def get_death_blow(cls, value: str) -> DeathBlow:
        return DeathBlow(text_to_float_div_100(value))

    @classmethod
    def get_trap(cls, value: str) -> Trap:
        return Trap(text_to_float_div_100(value))


class HeroResistanceModel:

    def __init__(self, factory):
        self.factory = factory
        self.stun: Stun or None = None
        self.move: Move or None = None
        self.blight: Blight or None = None
        self.bleed: Bleed or None = None
        self.disease: Disease or None = None
        self.debuff: Debuff or None = None
        self.death_blow: DeathBlow or None = None
        self.trap: Trap or None = None

    def set_values(self, stun=None, move=None, blight=None, bleed=None,
                   disease=None, debuff=None, death_blow=None, trap=None):
        self.stun = self.factory.get_stun(stun)
        self.move = self.factory.get_move(move)
        self.blight = self.factory.get_blight(blight)
        self.bleed = self.factory.get_bleed(bleed)
        self.disease = self.factory.get_disease(disease)
        self.debuff = self.factory.get_debuff(debuff)
        self.death_blow = self.factory.get_death_blow(death_blow)
        self.trap = self.factory.get_trap(trap)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}:\n{pretty(self.__dict__)}'
