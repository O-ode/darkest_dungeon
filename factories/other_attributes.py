from abc import ABC

from constants import pretty
from factories.attribute_base import BasicAttribute
from selenium_local.text_modifying_functions import do_nothing


class Movement(BasicAttribute):
    pass


class CritBuffBonus(BasicAttribute):
    pass


class Religious(BasicAttribute):
    pass


class Provisions(BasicAttribute):
    pass


class OtherHeroAttributesFactory(ABC):

    @classmethod
    def set_movement(cls, value: str):
        return Movement(do_nothing(value))

    @classmethod
    def set_crit_buff_bonus(cls, value: str):
        return CritBuffBonus(do_nothing(value))

    @classmethod
    def set_religious(cls, value: str):
        return Religious(do_nothing(value))

    @classmethod
    def set_provisions(cls, value: str):
        return Provisions(do_nothing(value))


class OtherHeroAttributes:
    def __init__(self, factory):
        self.factory: OtherHeroAttributesFactory = factory
        self.movement: Movement or None = None
        self.crit_buff_bonus: CritBuffBonus or None = None
        self.religious: Religious or None = None
        self.provisions: Provisions or None = None

    def set_values(self, movement, crit_buff_bonus, religious, provisions):
        self.movement = self.factory.set_movement(movement)
        self.crit_buff_bonus = self.factory.set_crit_buff_bonus(crit_buff_bonus)
        self.religious = self.factory.set_religious(religious)
        self.provisions = self.factory.set_provisions(provisions)

    def __repr__(self):
        return f'{self.__class__.__name__}:\n{pretty(self.__dict__)}'
