from typing import Any

from base_classes.character_attributes import Crit, AccMod
from base_classes.int_range import DmgRange
from base_classes.other_hero_attributes import Provisions, Religious, CritBuffBonus, Movement
from base_classes.resistances import Trap, DeathBlow, Debuff, Disease, Bleed, Blight, Move, Stun
from constants import pretty
from factories.hero_attributes_factories import OtherHeroAttributesFactory
from model.character_attributes.base_attributes import BaseLevelAttributesModel


class HeroLevelAttributesModel(BaseLevelAttributesModel):

    def __init__(self, factory):
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


class OtherHeroAttributes:
    def __init__(self, factory):
        self._factory: OtherHeroAttributesFactory = factory
        self._movement: Movement or None = None
        self._crit_buff_bonus: CritBuffBonus or None = None
        self._religious: Religious or None = None
        self._provisions: Provisions or None = None

    def set_movement(self, value: Any):
        self._movement = self._factory.prepare_movement(value)
        return self

    def get_movement(self):
        return self._movement

    def set_crit_buff_bonus(self, value: Any):
        self._crit_buff_bonus = self._factory.prepare_crit_buff_bonus(value)
        return self

    def get_crit_buff_bonus(self):
        return self._crit_buff_bonus

    def set_religious(self, value: Any):
        self._religious = self._factory.prepare_religious(value)
        return self

    def get_religious(self):
        return self._religious

    def set_provisions(self, value: Any):
        self._provisions = self._factory.prepare_provisions(value)
        return self

    def get_provisions(self):
        return self._provisions

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))


class HeroResistanceModel:

    def __init__(self, factory):
        self._factory = factory
        self._stun: Stun or None = None
        self._move: Move or None = None
        self._blight: Blight or None = None
        self._bleed: Bleed or None = None
        self._disease: Disease or None = None
        self._debuff: Debuff or None = None
        self._death_blow: DeathBlow or None = None
        self._trap: Trap or None = None

    def set_stun(self, value: Any):
        self._stun = self._factory.prepare_stun(value)
        return self

    def set_move(self, value: Any):
        self._move = self._factory.prepare_move(value)
        return self

    def set_blight(self, value: Any):
        self._blight = self._factory.prepare_blight(value)
        return self

    def set_bleed(self, value: Any):
        self._bleed = self._factory.prepare_bleed(value)
        return self

    def set_disease(self, value: Any):
        self._disease = self._factory.prepare_disease(value)
        return self

    def set_death_blow(self, value: Any):
        self._death_blow = self._factory.prepare_death_blow(value)
        return self

    def set_debuff(self, value: Any):
        self._debuff = self._factory.prepare_debuff(value)
        return self

    def set_trap(self, value: Any):
        self._trap = self._factory.prepare_trap(value)
        return self

    def get_stun(self):
        return self._stun

    def get_move(self):
        return self._move

    def get_blight(self):
        return self._blight

    def get_bleed(self):
        return self._bleed

    def get_disease(self):
        return self._disease

    def get_debuff(self):
        return self._debuff

    def get_death_blow(self):
        return self._death_blow

    def get_trap(self):
        return self._trap

    # def set(self, value: Any):
    #     self. = self._factory.prepare(value)
    #     return self
    #
    # def get(self):
    #     return self.

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
