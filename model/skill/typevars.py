from typing import TypeVar

from model.skill.enemy_skills.enemy_skill import EnemySkill
from model.skill.hero_combat_skills.hero_heal_combat_skill import HeroHealCombatSkill
from model.skill.hero_combat_skills.hero_offensive_combat_skill import HeroOffensiveCombatSkill

CombatSkillType = TypeVar("CombatSkillType", HeroOffensiveCombatSkill, HeroHealCombatSkill, EnemySkill)
