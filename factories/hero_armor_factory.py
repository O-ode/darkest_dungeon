import warnings

from base_classes.armor_attributes import Dodge, Prot, HP
from base_classes.common import Name
from factories.value_modifying_factory import ValueModifyingFactory


class HeroArmorFactory:

    @classmethod
    def prepare_name(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Name(value)

    @classmethod
    def prepare_dodge(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Dodge(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_prot(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Prot(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_hp(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return HP(ValueModifyingFactory.text_to_int(value))
