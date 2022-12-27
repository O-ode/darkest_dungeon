import re

from base_classes.armor_attributes import Dodge, HP
from base_classes.common import Name
from factories.value_modifying_factory import ValueModifyingFactory


class HeroArmorFactory:

    @classmethod
    def prepare_name(cls, value: str):
        return Name(re.search(r'[\s\w]+', value).group())

    @classmethod
    def prepare_dodge(cls, value: str):
        return Dodge(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_hp(cls, value: str):
        return HP(ValueModifyingFactory.text_to_int(value))
