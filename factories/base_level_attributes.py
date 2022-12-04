from abc import ABC, abstractmethod
from typing import Any

from constants import pretty
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class AttributeBase(ABC):
    value: Any

    def __repr__(self):
        return pretty(self.__dict__)


class HP(AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)


class Dodge(AttributeBase):
    value: float

    def __init__(self, value: str):
        self.value = text_to_float_div_100(value)


class Prot(AttributeBase):
    value: float

    def __init__(self, value: str):
        self.value = text_to_float_div_100(value)


class Spd(AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)


class BaseLevelAttributes:
    hp: HP
    dodge: Dodge
    prot: Prot
    spd: Spd


class BaseLevelAttributesFactory(ABC):
    @abstractmethod
    def get_hp(self, value: str) -> HP:
        pass

    @abstractmethod
    def get_dodge(self, value: str) -> Dodge:
        pass

    @abstractmethod
    def get_prot(self, value: str) -> Prot:
        pass

    @abstractmethod
    def get_spd(self, value: str) -> Spd:
        pass
