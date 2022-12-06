from abc import ABC
from typing import Any

from constants import pretty
from factories.attribute_base import AttributeBase
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class HP(AttributeBase):
    pass


class Dodge(AttributeBase):
    pass


class Prot(AttributeBase):
    pass


class Spd(AttributeBase):
    pass


class BaseLevelAttributes(ABC):
    hp: HP
    dodge: Dodge
    prot: Prot
    spd: Spd

    def __repr__(self):
        values_str = '\n\t'.join([pretty(v) for v in self.__dict__.values()])
        return f'{self.__class__.__name__}{{{values_str}\n}}'


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
