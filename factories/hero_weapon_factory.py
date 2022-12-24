from base_classes.character_attributes import Dodge, Prot, HP
from factories.value_modifying_factory import ValueModifyingFactory


class HeroWeaponFactory:

    @classmethod
    def prepare_name(cls, value: str):
        return value

    @classmethod
    def prepare_dodge(cls, value: str):
        return Dodge(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_prot(cls, value: str):
        return Prot(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_hp(cls, value: str):
        return HP(ValueModifyingFactory.text_to_int(value))
