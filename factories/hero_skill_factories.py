import warnings

from base_classes.skill_attributes import Heal, CritMod, Accuracy, DmgMod, SkillType, Level, Move
from constants import SkillBooleans
from factories.base_skill_factories import BaseSkillFactory
from factories.value_modifying_factory import ValueModifyingFactory

warnings.warn("File to be updated", DeprecationWarning)


class HeroSkillFactory(BaseSkillFactory):
    @classmethod
    def prepare_move(cls, values: list[str]):
        return Move(int(values[0]), int(values[1]))

    @classmethod
    def prepare_skill_booleans(cls, **values):
        return SkillBooleans(ValueModifyingFactory.merge_skill_booleans(**values))

    @classmethod
    def prepare_skill_type(cls, value: str):
        return SkillType(ValueModifyingFactory.str_to_skill_type(value))

    @classmethod
    def prepare_dmg_mod(cls, values: list[str]):
        return [DmgMod(ValueModifyingFactory.text_to_float_div_100(v)) for v in values]

    @classmethod
    def prepare_acc(cls, values: list[str]):
        return [Accuracy(ValueModifyingFactory.text_to_float_div_100(v)) for v in values]

    @classmethod
    def prepare_crit_mod(cls, values: list[str]):
        return [CritMod(ValueModifyingFactory.text_to_float_div_100(v)) for v in values]

    @classmethod
    def prepare_heal(cls, values: list[str]):
        return [Heal(ValueModifyingFactory.text_to_hp_modification_value(v)) for v in values]

    @classmethod
    def prepare_level(cls, value: str):
        return Level(ValueModifyingFactory.text_to_int(value))

    @classmethod
    def prepare_on_other_heroes(cls, values: list[str]):
        return [ValueModifyingFactory.text_to_effect_list(value) for value in values]


class CampingSkillFactory:

    @classmethod
    def prepare_skill_name(cls, value: str):
        return ValueModifyingFactory.do_nothing(value)

    @classmethod
    def prepare_time_cost(cls, value: str):
        return ValueModifyingFactory.text_to_int(value)

    @classmethod
    def prepare_target(cls, value: str):
        return ValueModifyingFactory.do_nothing(value)

    @classmethod
    def prepare_description(cls, value: str):
        return ValueModifyingFactory.text_to_effect_list(value)
