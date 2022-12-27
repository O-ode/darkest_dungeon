from typing import Any

from base_classes.armor_attributes import Dodge, HP
from base_classes.common import Name
from constants import pretty
from factories.hero_armor_factory import HeroArmorFactory


class Armor:

    def __init__(self, factory):
        self._factory: HeroArmorFactory = factory
        self._name: Name or None = None
        self._dodge: Dodge or None = None
        self._hp: HP or None = None

    def set_name(self, value: Any):
        self._name = self._factory.prepare_name(value)
        return self

    def set_dodge(self, value: Any):
        self._dodge = self._factory.prepare_dodge(value)
        return self

    def set_hp(self, value: Any):
        self._hp = self._factory.prepare_hp(value)
        return self

    def get_name(self):
        return self._name

    def get_dodge(self):
        return self._dodge

    def get_hp(self):
        return self._hp

    def __repr__(self):
        return pretty(vars(self))
