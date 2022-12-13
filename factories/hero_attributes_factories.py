from abc import ABC

from base_classes.character_attributes import Crit, AccMod, Level
from base_classes.int_range import DmgRange
from base_classes.other_hero_attributes import Provisions, Religious, CritBuffBonus, Movement
from base_classes.resistances import Trap, DeathBlow, Debuff, Disease, Bleed, Blight, Move, Stun
from constants import pretty
from factories.base_attributes_factories import BaseLevelAttributesFactory
from factories.value_modifying_factory import ValueModifyingFactory


class HerolevelAttributesFactory(BaseLevelAttributesFactory):

    @classmethod
    def prepare_level(cls, value: str) -> Level:
        return Level(ValueModifyingFactory.text_to_int(value))

    @classmethod
    def prepare_acc_mod(cls, value: str) -> AccMod:
        return AccMod(ValueModifyingFactory.text_to_int(value))

    @classmethod
    def prepare_crit(cls, value: str) -> Crit:
        return Crit(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_dmg(cls, value: str) -> DmgRange:
        return DmgRange(*ValueModifyingFactory.text_to_int_range(value))


class OtherHeroAttributesFactory(ABC):

    @classmethod
    def prepare_movement(cls, value: str):
        return Movement(ValueModifyingFactory.do_nothing(value))

    @classmethod
    def prepare_crit_buff_bonus(cls, value: str):
        return CritBuffBonus(ValueModifyingFactory.do_nothing(value))

    @classmethod
    def prepare_religious(cls, value: str):
        return Religious(ValueModifyingFactory.do_nothing(value))

    @classmethod
    def prepare_provisions(cls, value: str):
        return Provisions(ValueModifyingFactory.do_nothing(value))

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))


class ResistancesFactory(ABC):

    @classmethod
    def prepare_stun(cls, value: str) -> Stun:
        return Stun(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_move(cls, value: str) -> Move:
        return Move(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_blight(cls, value: str) -> Blight:
        return Blight(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_bleed(cls, value: str) -> Bleed:
        return Bleed(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_disease(cls, value: str) -> Disease:
        return Disease(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_debuff(cls, value: str) -> Debuff:
        return Debuff(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_death_blow(cls, value: str) -> DeathBlow:
        return DeathBlow(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_trap(cls, value: str) -> Trap:
        return Trap(ValueModifyingFactory.text_to_float_div_100(value))
