from typing import Any, Type

from base_classes.character_attributes import Crit, AccMod
from base_classes.int_range import DmgRange
from base_classes.other_hero_attributes import Provisions, Religious, CritBuffBonus, Movement
from base_classes.resistances import Trap, DeathBlow, Debuff, Disease, Bleed, Blight, Move, Stun
from constants import pretty
from factories.hero_attributes_factories import OtherHeroAttributesFactory, HeroLevelAttributesFactory
from model.character_attributes.base_attributes import BaseLevelAttributesModel


class HeroLevelAttributesModel(BaseLevelAttributesModel):

    def __init__(self, factory: Type[HeroLevelAttributesFactory]):
        super(HeroLevelAttributesModel, self).__init__(factory)
        self._acc_mod: AccMod or None = None
        self._crit: Crit or None = None
        self._dmg: DmgRange or None = None

    def set_acc_mod(self, value: Any):
        self._acc_mod = self._factory.prepare_acc_mod(value)
        return self

    def set_crit(self, value: Any):
        self._crit = self._factory.prepare_crit(value)
        return self

    def set_dmg(self, value: Any):
        self._dmg = self._factory.prepare_dmg(value)
        return self

    def get_acc_mod(self):
        return self._acc_mod

    def get_crit(self):
        return self._crit

    def get_dmg(self):
        return self._dmg
