from typing import Any

from base_classes.skill_attributes import Heal
from factories.hero_skill_factories import HeroSkillFactory
from model.skill.hero_combat_skills.hero_combat_base_skill import HeroCombatBaseSkill


class HeroCombatHealSkill(HeroCombatBaseSkill):

    def __init__(self, factory: HeroSkillFactory):
        super(HeroCombatHealSkill, self).__init__(factory)
        self._heal: Heal or None = None

    def get_heal(self):
        return self._heal

    def set_heal(self, value: Any):
        self._heal = self._factory.prepare_heal(value)
