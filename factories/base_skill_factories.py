from base_classes.common import Name
from base_classes.skill_attributes import Limit, Launch, Target
from factories.value_modifying_factory import ValueModifyingFactory


class BaseSkillFactory:

    @classmethod
    def prepare_skill_name(cls, value: str):
        return Name(value)

    @classmethod
    def prepare_launch(cls, values: str):
        return Launch(ValueModifyingFactory.str_to_position_flag(values))

    @classmethod
    def prepare_target(cls, values: str):
        return Target(ValueModifyingFactory.str_to_position_flag(values))

    @classmethod
    def prepare_limit(cls, value: str):
        if value:
            return Limit(ValueModifyingFactory.text_to_one_int_from_regex(value))
        else:
            return None
