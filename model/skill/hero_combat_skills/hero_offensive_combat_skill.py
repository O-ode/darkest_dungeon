from typing import Any, Type

from base_classes.skill_attributes import CritMod, DmgMod, Accuracy, SkillType, Move
from factories.hero_skill_factories import HeroSkillFactory
from model.skill.hero_combat_skills.hero_combat_base_skill import HeroCombatBaseSkill


class HeroOffensiveCombatSkill(HeroCombatBaseSkill):

    def __init__(self, factory: Type[HeroSkillFactory]):
        super(HeroOffensiveCombatSkill, self).__init__(factory)
        self._skill_type: SkillType or None = None
        self._acc: Accuracy or None = None
        self._dmg_mod: DmgMod or None = None
        self._crit_mod: CritMod or None = None
        self._move: Move or None = None

    def set_move(self, values: list[Any]):
        self._move = self._factory.prepare_move(values)

    def set_skill_type(self, value: Any):
        self._skill_type = self._factory.prepare_skill_type(value)
        return self

    def set_acc(self, value: Any):
        self._acc = self._factory.prepare_acc(value)
        return self

    def set_dmg_mod(self, value: Any):
        self._dmg_mod = self._factory.prepare_dmg_mod(value)
        return self

    def set_crit_mod(self, value: Any):
        self._crit_mod = self._factory.prepare_crit_mod(value)
        return self

    def get_skill_type(self):
        return self._skill_type

    def get_acc(self):
        return self._acc

    def get_dmg_mod(self):
        return self._dmg_mod

    def get_crit_mod(self):
        return self._crit_mod
