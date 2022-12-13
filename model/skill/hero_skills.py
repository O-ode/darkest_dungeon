from typing import Any, Type

from base_classes.skill_attributes import CritMod, Accuracy, DmgMod, Range, Heal, Limit, Effect
from factories.hero_skill_factories import HeroSkillFactory
from model.skill.base_skill import BaseSkill


class HeroBaseSkill(BaseSkill):
    def __init__(self, factory: Type[HeroSkillFactory]):
        super(HeroBaseSkill, self).__init__(factory)
        self._limit: Limit or None = None
        self._on_other_heroes: list[list[Effect]] or None = None

    def set_limit(self, value: Any):
        self._limit = self._factory.prepare_limit(value)
        return self

    def set_on_other_heroes(self, values: list[Any]):
        self._on_other_heroes = self._factory.prepare_on_other_heroes(values)
        return self

    def get_limit(self):
        return self._limit

    def get_on_other_heroes(self):
        return self._on_other_heroes


class HeroSupportSkill(HeroBaseSkill):
    pass


class HeroHealSkill(HeroBaseSkill):

    def __init__(self, factory):
        super(HeroHealSkill, self).__init__(factory)
        self._heal: list[Heal] or None = None

    def set_heal(self, values: list[Any]):
        self._heal = self._factory.prepare_heal(values)
        return self

    def get_heal(self):
        return self._heal


class HeroOffensiveSkill(HeroBaseSkill):
    def __init__(self, factory):
        super(HeroOffensiveSkill, self).__init__(factory)
        self._on_range: Range or None = None
        self._dmg_mod: list[DmgMod] or None = None
        self._acc: list[Accuracy] or None = None
        self._crit_mod: list[CritMod] or None = None

    def set_on_range(self, value: Any):
        self._on_range = self._factory.prepare_on_range(value)
        return self

    def set_dmg_mod(self, values: list[Any]):
        self._dmg_mod = self._factory.prepare_dmg_mod(values)
        return self

    def set_acc(self, values: list[Any]):
        self._acc = self._factory.prepare_acc(values)
        return self

    def set_crit_mod(self, values: list[Any]):
        self._crit_mod = self._factory.prepare_crit_mod(values)
        return self

    def get_on_range(self):
        return self._on_range

    def get_dmg_mod(self):
        return self._dmg_mod

    def get_acc(self):
        return self._acc

    def get_crit_mod(self):
        return self._crit_mod

    # def set(self, value: Any):
    #     self. = self._factory.prepare(value)
    #
    # def get(self):
    #     return self.
