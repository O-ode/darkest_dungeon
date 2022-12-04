from constants import pretty
from factories import base_level_attributes
from factories.base_level_attributes import HP, Dodge, Prot, Spd
from selenium_local.text_modifying_functions import text_to_int, text_to_float_div_100


class AccMod(base_level_attributes.AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)


class Crit(base_level_attributes.AttributeBase):
    value: float

    def __init__(self, value: str):
        self.value = text_to_float_div_100(value)


class MinDmg(base_level_attributes.AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)


class MaxDmg(base_level_attributes.AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)


class ResolveLevel(base_level_attributes.AttributeBase):
    value: int

    def __init__(self, value: str):
        self.value = text_to_int(value)

    def __hash__(self):
        return hash(self.value)


class HeroResolveLevelAttributesFactory(base_level_attributes.BaseLevelAttributesFactory):

    def get_hp(self, value: str) -> HP:
        return HP(value)

    def get_dodge(self, value: str) -> Dodge:
        return Dodge(value)

    def get_prot(self, value: str) -> Prot:
        return Prot(value)

    def get_spd(self, value: str) -> Spd:
        return Spd(value)

    def get_resolve_level(self, value: str) -> ResolveLevel:
        return ResolveLevel(value)

    def get_acc_mod(self, value: str) -> AccMod:
        return AccMod(value)

    def get_crit(self, value: str) -> Crit:
        return Crit(value)

    def get_min_dmg(self, value: str) -> MinDmg:
        return MinDmg(value)

    def get_max_dmg(self, value: str) -> MaxDmg:
        return MaxDmg(value)

    def get_max_dmg_and_min_dmg(self, value: str) -> (MaxDmg, MinDmg):
        split = value.split("-")
        _max = split[0]
        _min = split[1]
        return self.get_max_dmg(_max), self.get_min_dmg(_min)


class HeroResolveLevelAttributes(base_level_attributes.BaseLevelAttributes):
    factory: HeroResolveLevelAttributesFactory
    acc_mod: AccMod
    crit: Crit
    min_dmg: MinDmg
    max_dmg: MaxDmg
    resolve_level: ResolveLevel

    def __init__(self, factory: HeroResolveLevelAttributesFactory):
        self.factory = factory

    def get_values(self, resolve_level: int, max_hp=None, dodge=None, prot=None,
                   spd=None, acc_mod=None, crit=None, dmg=None):
        self.resolve_level = self.factory.get_resolve_level(str(resolve_level))  # TODO: REFACTOR THIS
        self.hp = self.factory.get_hp(max_hp)
        self.dodge = self.factory.get_dodge(dodge)
        self.prot = self.factory.get_prot(prot)
        self.spd = self.factory.get_spd(spd)
        self.acc_mod = self.factory.get_acc_mod(acc_mod)
        self.crit = self.factory.get_crit(crit)
        self.max_dmg, self.min_dmg = self.factory.get_max_dmg_and_min_dmg(dmg)
        return self

    def __repr__(self):
        return pretty(self.__dict__)
