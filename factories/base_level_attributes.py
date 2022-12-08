from abc import ABC

from constants import pretty
from factories.attribute_base import BasicAttribute
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class HP(BasicAttribute):
    pass


class Dodge(BasicAttribute):
    pass


class Prot(BasicAttribute):
    pass


class Spd(BasicAttribute):
    pass


class BaseLevelAttributes(ABC):
    hp: HP
    dodge: Dodge
    prot: Prot
    spd: Spd


class BaseLevelAttributesFactory(ABC):
    @classmethod
    def set_hp(cls, value: str) -> HP:
        return HP(text_to_int(value))

    @classmethod
    def set_dodge(cls, value: str) -> Dodge:
        return Dodge(text_to_float_div_100(value))

    @classmethod
    def set_prot(cls, value: str) -> Prot:
        return Prot(text_to_float_div_100(value))

    @classmethod
    def set_spd(cls, value: str) -> Spd:
        return Spd(text_to_int(value))


    def __repr__(self):
        return f'{self.__class__.__name__}:\n{pretty(self.__dict__)}'