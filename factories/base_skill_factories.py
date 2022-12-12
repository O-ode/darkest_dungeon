import re

from base_classes.skill_attributes import Limit, Effect, Rank, SkillName, Target
from factories.value_modifying_factory import ValueModifyingFactory


class BaseSkillFactory:
    @classmethod
    def prepare_skill_name(cls, value: str):
        return SkillName(value)

    @classmethod
    def prepare_rank(cls, values: list[int]):
        return Rank(ValueModifyingFactory.int_array_to_position_flag(value))

    @classmethod
    def prepare_target(cls, values: list[int]):
        return Target(ValueModifyingFactory.int_array_to_position_flag(value))

    @classmethod
    def prepare_on_target(cls, values: list[str]):
        effects_str = []
        for v in re.split(r'\n', value):
            p = v.replace(r'\n', '')
            if p != '':
                effects_str.append(p)
        return [Effect(s) for s in effects_str]

    @classmethod
    def prepare_on_self(cls, values: list[str]):
        effects_str = []
        for v in re.split(r'\n', value):
            p = v.replace(r'\n', '')
            if p != '':
                effects_str.append(p)
        return [Effect(s) for s in effects_str]

    @classmethod
    def prepare_limit(cls, value: str):
        if value:
            return Limit(ValueModifyingFactory.text_to_one_int_from_regex(value))
        else:
            return None
