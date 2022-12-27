from typing import Any, Type

from base_classes.skill_attributes import Heal
from factories.hero_skill_factories import HeroSkillFactory
from model.skill.hero_combat_skills.hero_combat_base_skill import HeroCombatBaseSkill


class HeroHealCombatSkill(HeroCombatBaseSkill):

    def __init__(self, factory: Type[HeroSkillFactory]):
        super(HeroHealCombatSkill, self).__init__(factory)
        self._heal: Heal or None = None

    def get_heal(self):
        return self._heal

    def set_heal(self, value: Any):
        self._heal = self._factory.prepare_heal(value)
        return self
