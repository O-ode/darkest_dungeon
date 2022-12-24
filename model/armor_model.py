from typing import Any

from base_classes.character_attributes import Crit, Spd
from base_classes.common import Name
from base_classes.int_range import DmgRange
from factories.hero_armor_factory import HeroArmorFactory


class Armor:

    def __init__(self, factory):
        self._factory: HeroArmorFactory = factory
        self._name: Name or None = None
        self._dmg: DmgRange or None = None
        self._crit: Crit or None = None
        self._spd: Spd or None = None

    def set_name(self, value: Any):
        self._name = self._factory.prepare_name(value)

    def set_dmg(self, value: Any):
        self._dmg = self._factory.prepare_dmg(value)

    def set_crit(self, value: Any):
        self._crit = self._factory.prepare_crit(value)

    def set_spd(self, value: Any):
        self._spd = self._factory.prepare_spd(value)

    def get_name(self):
        return self._name

    def get_dmg(self):
        return self._dmg

    def get_crit(self):
        return self._crit

    def get_spd(self):
        return self._spd
