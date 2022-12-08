from typing import Type, Any

from constants import pretty, RangeEnum
from factories.attribute_base import BasicAttribute
from model.effect_model import EffectModel
from selenium_local.text_modifying_functions import text_to_float_div_100, text_to_int, text_to_effects_dict, \
    text_to_effect_per_line


class Range(BasicAttribute):
    pass


class Rank(BasicAttribute):
    pass


class Target(BasicAttribute):
    pass


class DmgMod(BasicAttribute):
    pass


class Accuracy(BasicAttribute):
    pass


class CritMod(BasicAttribute):
    pass


class Effects(BasicAttribute):
    pass


class OnSelf(BasicAttribute):
    pass


class Heal(BasicAttribute):
    pass


class SkillFactory:
    @classmethod
    def prepare_skill_name(cls, value: str):
        return value

    @classmethod
    def prepare_on_range(cls, value: str):
        return Range(RangeEnum.from_string(value))

    @classmethod
    def prepare_rank(cls, value: [int]):
        return Rank(value)

    @classmethod
    def prepare_target(cls, value: [int]):
        return Target(value)

    @classmethod
    def prepare_dmg_mod(cls, value: str):
        return DmgMod(text_to_float_div_100(value))

    @classmethod
    def prepare_acc(cls, value: str):
        return Accuracy(text_to_int(value))

    @classmethod
    def prepare_crit_mod(cls, value: str):
        return CritMod(text_to_float_div_100(value))

    @classmethod
    def prepare_effects(cls, value: str):
        return Effects(text_to_effects_dict(value))

    @classmethod
    def prepare_on_self(cls, value: str):
        return Effects(text_to_effect_per_line(value))

    @classmethod
    def prepare_heal(cls, value: str):
        return Heal(text_to_int(value))


class SkillModel:
    def __init__(self, factory: Type[SkillFactory], skill_name: str = None):
        self.factory: Type[SkillFactory] = factory
        self.skill_name: str or None = skill_name
        self.on_range: Range or None = None
        self.rank: [int] or None = None
        self.target: [int] or str or None = None
        self.dmg_mod: float or None = None
        self.acc: int or None = None
        self.crit_mod: float or None = None
        self.effects: {str: list[EffectModel]} or None = None
        self.on_self: [EffectModel] or None = None
        self.heal: int or None = None

    def set_skill_name(self, value: Any):
        self.skill_name = self.factory.set_(value)
        return self

    def set_on_range(self, value: Any):
        self.on_range = self.factory.set_(value)
        return self

    def set_rank(self, value: Any):
        self.rank = self.factory.set_(value)
        return self

    def set_target(self, value: Any):
        self.target = self.factory.set_(value)
        return self

    def set_dmg_mod(self, value: Any):
        self.dmg_mod = self.factory.set_(value)
        return self

    def set_acc(self, value: Any):
        self.acc = self.factory.set_(value)
        return self

    def set_crit_mod(self, value: Any):
        self.crit_mod = self.factory.set_(value)
        return self

    def set_effects(self, value: Any):
        self.effects = self.factory.set_(value)
        return self

    def set_on_self(self, value: Any):
        self.on_self = self.factory.set_(value)
        return self

    def set_heal(self, value: Any):
        self.heal = self.factory.set_(value)
        return self

    def __repr__(self):
        return pretty(self.__dict__)

    def __str__(self):
        return pretty(self.__dict__)

    def __hash__(self):
        return hash(self.skill_name)
