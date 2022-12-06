from factories.attribute_base import AttributeBase
from factories.base_level_attributes import BaseLevelAttributes, BaseLevelAttributesFactory
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class AccMod(AttributeBase):
    pass


class Crit(AttributeBase):
    pass


class MinDmg(AttributeBase):
    pass


class MaxDmg(AttributeBase):
    pass


class ResolveLevel(AttributeBase):
    pass

    def __hash__(self):
        return hash(self.value)


class HeroResolveLevelAttributesFactory(BaseLevelAttributesFactory):

    @classmethod
    def set_resolve_level(cls, value: str) -> ResolveLevel:
        return ResolveLevel(text_to_int(value))

    @classmethod
    def set_acc_mod(cls, value: str) -> AccMod:
        return AccMod(text_to_int(value))

    @classmethod
    def set_crit(cls, value: str) -> Crit:
        return Crit(text_to_float_div_100(value))

    @classmethod
    def set_min_dmg(cls, value: str) -> MinDmg:
        return MinDmg(text_to_int(value))

    @classmethod
    def set_max_dmg(cls, value: str) -> MaxDmg:
        return MaxDmg(text_to_int(value))

    @classmethod
    def set_max_dmg_and_min_dmg(cls, value: str) -> (MaxDmg, MinDmg):
        split = value.split("-")
        _max = split[0]
        _min = split[1]
        return cls.set_max_dmg(_max), cls.set_min_dmg(_min)


class HeroResolveLevelAttributes(BaseLevelAttributes):

    def __init__(self, factory: HeroResolveLevelAttributesFactory):
        self.factory = factory
        self.acc_mod: AccMod or None = None
        self.crit: Crit or None = None
        self.min_dmg: MinDmg or None = None
        self.max_dmg: MaxDmg or None = None
        self.resolve_level: ResolveLevel or None = None

    def set_values(self, resolve_level: int, max_hp=None, dodge=None, prot=None,
                   spd=None, acc_mod=None, crit=None, dmg=None):
        self.resolve_level = self.factory.set_resolve_level(str(resolve_level))  # TODO: REFACTOR THIS
        self.hp = self.factory.set_hp(max_hp)
        self.dodge = self.factory.set_dodge(dodge)
        self.prot = self.factory.set_prot(prot)
        self.spd = self.factory.set_spd(spd)
        self.acc_mod = self.factory.set_acc_mod(acc_mod)
        self.crit = self.factory.set_crit(crit)
        self.max_dmg, self.min_dmg = self.factory.set_max_dmg_and_min_dmg(dmg)
        return self
