from base_classes.character_attributes import Crit, Spd
from base_classes.int_range import DmgRange
from factories.value_modifying_factory import ValueModifyingFactory


class HeroArmorFactory:

    @classmethod
    def prepare_name(cls, value: str):
        return value

    @classmethod
    def prepare_dmg(cls, value: str):
        return DmgRange(*ValueModifyingFactory.text_to_int_range(value))

    @classmethod
    def prepare_crit(cls, value: str):
        return Crit(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_spd(cls, value: str):
        return Spd(ValueModifyingFactory.text_to_int(value))
