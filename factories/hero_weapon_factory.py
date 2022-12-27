import warnings

from base_classes.weapon_attributes import Dmg, Crit, Spd
from factories.value_modifying_factory import ValueModifyingFactory


class HeroWeaponFactory:

    @classmethod
    def prepare_name(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return value

    @classmethod
    def prepare_dmg(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Dmg(*ValueModifyingFactory.text_to_int_range(value))

    @classmethod
    def prepare_crit(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Crit(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_spd(cls, value: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return Spd(ValueModifyingFactory.text_to_int(value))
