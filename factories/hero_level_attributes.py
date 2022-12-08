from constants import pretty
from factories.attribute_base import BasicAttribute, IntRange
from factories.base_level_attributes import BaseLevelAttributes, BaseLevelAttributesFactory
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class AccMod(BasicAttribute):
    pass


class Crit(BasicAttribute):
    pass


class DmgRange(IntRange):
    pass


class HeroResolveAttributesFactory(BaseLevelAttributesFactory):

    @classmethod
    def set_acc_mod(cls, value: str) -> AccMod:
        return AccMod(text_to_int(value))

    @classmethod
    def set_crit(cls, value: str) -> Crit:
        return Crit(text_to_float_div_100(value))

    @classmethod
    def set_dmg(cls, value: str) -> DmgRange:
        split = value.split("-")
        lower = text_to_int(split[0])
        upper = text_to_int(split[1])
        return DmgRange(upper, lower)


class HeroResolveAttributesModel(BaseLevelAttributes):

    def __init__(self, factory):
        self.factory = factory
        self.acc_mod: AccMod or None = None
        self.crit: Crit or None = None
        self.dmg: DmgRange or None = None

    def set_values(self, max_hp=None, dodge=None, prot=None,
                   spd=None, acc_mod=None, crit=None, dmg=None):
        self.hp = self.factory.set_hp(max_hp)
        self.dodge = self.factory.set_dodge(dodge)
        self.prot = self.factory.set_prot(prot)
        self.spd = self.factory.set_spd(spd)
        self.acc_mod = self.factory.set_acc_mod(acc_mod)
        self.crit = self.factory.set_crit(crit)
        self.dmg = self.factory.set_dmg(dmg)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}:\n{pretty(self.__dict__)}'
