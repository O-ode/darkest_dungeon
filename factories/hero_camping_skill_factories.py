import warnings

from factories.value_modifying_factory import ValueModifyingFactory


class CampingSkillFactory:

    @classmethod
    def prepare_skill_name(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return ValueModifyingFactory.do_nothing(value)

    @classmethod
    def prepare_time_cost(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return ValueModifyingFactory.text_to_int(value)

    @classmethod
    def prepare_target(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return ValueModifyingFactory.do_nothing(value)

    @classmethod
    def prepare_description(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return ValueModifyingFactory.text_to_effect_list(value)
