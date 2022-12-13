from base_classes.skill_attributes import Limit, Rank, SkillName, Target
from factories.value_modifying_factory import ValueModifyingFactory


class BaseSkillFactory:
    @classmethod
    def prepare_skill_name(cls, value: str):
        return SkillName(value)

    @classmethod
    def prepare_rank(cls, values: list[int]):
        return Rank(ValueModifyingFactory.int_array_to_position_flag(values))

    @classmethod
    def prepare_target(cls, values: list[int]):
        return Target(ValueModifyingFactory.int_array_to_position_flag(values))

    @classmethod
    def prepare_on_target(cls, values: list[str]):
        return [ValueModifyingFactory.text_to_effect_list(value) for value in values]

    @classmethod
    def prepare_on_self(cls, values: list[str]):
        return [ValueModifyingFactory.text_to_effect_list(value) for value in values]

    @classmethod
    def prepare_limit(cls, value: str):
        if value:
            return Limit(ValueModifyingFactory.text_to_one_int_from_regex(value))
        else:
            return None
