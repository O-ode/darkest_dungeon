from abc import ABC

from base_classes.resistances import Trap, DeathBlow, Debuff, Disease, Bleed, Blight, Move, Stun
from factories.value_modifying_factory import ValueModifyingFactory


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
