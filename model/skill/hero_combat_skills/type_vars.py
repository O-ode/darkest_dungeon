from typing import TypeVar

from model.skill.hero_combat_skills.hero_heal_combat_skill import HeroCombatHealSkill
from model.skill.hero_combat_skills.hero_offensive_combat_skill import HeroOffensiveCombatSkill

HeroSkill = TypeVar("HeroSkill", HeroOffensiveCombatSkill, HeroCombatHealSkill)
DerivedFromBaseSkill = TypeVar("DerivedFromBaseSkill", HeroOffensiveCombatSkill, HeroCombatHealSkill)