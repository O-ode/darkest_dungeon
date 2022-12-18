from abc import ABC
from typing import Any

from base_classes.character_attributes import HP, Dodge, Prot, Spd, Level
from constants import pretty
from model.skill.type_vars import CharacterModelFactories


class BaseLevelAttributesModel(ABC):

    def __init__(self, factory):
        self._factory: CharacterModelFactories = factory
        self._level: Level or None = None
        self._hp: HP or None = None
        self._dodge: Dodge or None = None
        self._prot: Prot or None = None
        self._spd: Spd or None = None

    def set_hp(self, value: Any):
        self._hp = self._factory.prepare_hp(value)
        return self

    def set_dodge(self, value: Any):
        self._dodge = self._factory.prepare_dodge(value)
        return self

    def set_prot(self, value: Any):
        self._prot = self._factory.prepare_prot(value)
        return self

    def set_spd(self, value: Any):
        self._spd = self._factory.prepare_spd(value)
        return self

    def set_level(self, value: Any):
        self._level = self._factory.prepare_level(value)
        return self

    def get_level(self):
        return self._level

    def get_hp(self):
        return self._hp

    def get_dodge(self):
        return self._dodge

    def get_prot(self):
        return self._prot

    def get_spd(self):
        return self._spd

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
