import re

from base_classes.basic_attribute import Name
from base_classes.stats_attributes import Spd
from base_classes.weapon_attributes import Dmg, Crit
from factories.value_modifying_factory import ValueModifyingFactory


class HeroWeaponFactory:

    @classmethod
    def prepare_name(cls, value: str):
        return Name(re.search(r'[\s\w]+', value).group())

    @classmethod
    def prepare_dmg(cls, values: list[str]):
        return Dmg(int(values[0]), int(values[1]))

    @classmethod
    def prepare_crit(cls, value: str):
        return Crit(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_spd(cls, value: str):
        return Spd(ValueModifyingFactory.text_to_int(value))
