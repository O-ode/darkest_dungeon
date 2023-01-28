from typing import Any, Type

from base_classes.basic_attribute import Name
from base_classes.stats_attributes import Spd
from base_classes.weapon_attributes import Dmg, Crit
from constants import pretty
from factories.hero_weapon_factory import HeroWeaponFactory


class Weapon:

    def __init__(self, factory: Type[HeroWeaponFactory]):
        self._factory: Type[HeroWeaponFactory] = factory
        self._name: Name or None = None
        self._dmg: Dmg or None = None
        self._crit: Crit or None = None
        self._spd: Spd or None = None

    def set_name(self, value: Any):
        self._name = self._factory.prepare_name(value)
        return self

    def set_dmg(self, value: Any):
        self._dmg = self._factory.prepare_dmg(value)
        return self

    def set_crit(self, value: Any):
        self._crit = self._factory.prepare_crit(value)
        return self

    def set_spd(self, value: Any):
        self._spd = self._factory.prepare_spd(value)
        return self

    def get_name(self) -> Name:
        return self._name

    def get_dmg(self) -> Dmg:
        return self._dmg

    def get_crit(self) -> Crit:
        return self._crit

    def get_spd(self) -> Spd:
        return self._spd

    def __repr__(self):
        return pretty(vars(self))
