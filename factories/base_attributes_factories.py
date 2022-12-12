import logging
from abc import ABC

from base_classes.character_attributes import Spd, Prot, Dodge, HP
from constants import pretty
from factories.value_modifying_factory import ValueModifyingFactory

logger = logging.getLogger()


class BaseLevelAttributesFactory(ABC):

    @classmethod
    def prepare_hp(cls, value: str) -> HP:
        return HP(ValueModifyingFactory.text_to_int(value))

    @classmethod
    def prepare_dodge(cls, value: str) -> Dodge:
        return Dodge(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_prot(cls, value: str) -> Prot:
        return Prot(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_spd(cls, value: str) -> Spd:
        return Spd(ValueModifyingFactory.text_to_int(value))

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
