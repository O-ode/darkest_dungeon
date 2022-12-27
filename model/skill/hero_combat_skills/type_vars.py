from typing import TypeVar

from model.skill.hero_combat_skills.hero_heal_combat_skill import HeroHealCombatSkill
from model.skill.hero_combat_skills.hero_offensive_combat_skill import HeroOffensiveCombatSkill

HeroCombatSkillTypes = TypeVar("HeroCombatSkillTypes", HeroOffensiveCombatSkill, HeroHealCombatSkill)
