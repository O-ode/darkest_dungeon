from typing import Any

from base_classes.character_attributes import Dodge, Prot, HP
from base_classes.common import Name
from factories.hero_weapon_factory import HeroWeaponFactory


class Weapon:

    def __init__(self, factory):
        self._factory: HeroWeaponFactory = factory
        self._name: Name or None = None
        self._dodge: Dodge or None = None
        self._prot: Prot or None = None
        self._hp: HP or None = None

    def set_name(self, value: Any):
        self._name = self._factory.prepare_name(value)

    def set_dodge(self, value: Any):
        self._dodge = self._factory.prepare_dodge(value)

    def set_prot(self, value: Any):
        self._prot = self._factory.prepare_prot(value)

    def set_hp(self, value: Any):
        self._hp = self._factory.prepare_hp(value)

    def get_name(self):
        return self._name

    def get_dodge(self):
        return self._dodge

    def get_prot(self):
        return self._prot

    def get_hp(self):
        return self._hp
