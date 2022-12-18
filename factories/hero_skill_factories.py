from base_classes.skill_attributes import Heal, CritMod, Accuracy, DmgMod, Range
from factories.base_skill_factories import BaseSkillFactory
from factories.value_modifying_factory import ValueModifyingFactory


class HeroSkillFactory(BaseSkillFactory):

    @classmethod
    def prepare_on_range(cls, value: str):
        return Range(ValueModifyingFactory.str_to_range_enum(value))

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
