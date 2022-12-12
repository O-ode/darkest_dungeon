import re

from base_classes.skill_attributes import Effect, Heal, CritMod, Accuracy, DmgMod, Range
from factories.base_skill_factories import BaseSkillFactory
from factories.value_modifying_factory import ValueModifyingFactory


class HeroSkillFactory(BaseSkillFactory):

    @classmethod
    def prepare_on_range(cls, value: str):
        return Range(ValueModifyingFactory.str_to_range_enum(value)

    @classmethod
    def prepare_dmg_mod(cls, values: list[str]):
        return DmgMod(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_acc(cls, values: list[str]):
        return Accuracy(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_crit_mod(cls, values: list[str]):
        return CritMod(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_heal(cls, values: list[str]):
        modified_value = ValueModifyingFactory.text_to_hp_modification_value(value)
        return Heal(modified_value)

    @classmethod
    def prepare_on_other_heroes(cls, values: list[str]):
        effects_str = []
        for v in re.split(r'\n', value):
            p = v.replace(r'\n', '')
            if p != '':
                effects_str.append(p)

        return [Effect(s) for s in effects_str]
