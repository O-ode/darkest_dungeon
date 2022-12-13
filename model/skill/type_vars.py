from typing import TypeVar

from model.skill.base_skill import BaseSkill
from model.skill.enemy_skills import EnemyBaseSkill, EnemySupportSkill, EnemyOffensiveSkill
from model.skill.hero_skills import HeroBaseSkill, HeroOffensiveSkill, HeroSupportSkill, HeroHealSkill


DerivedFromBaseSkill = TypeVar("DerivedFromBaseSkill", BaseSkill, HeroBaseSkill, HeroOffensiveSkill,
                               HeroSupportSkill, HeroHealSkill, EnemyBaseSkill, EnemySupportSkill,
                               EnemyOffensiveSkill)

DerivedFromHeroBaseSkill = TypeVar("DerivedFromHeroBaseSkill", HeroBaseSkill, HeroOffensiveSkill, HeroSupportSkill,
                                   HeroHealSkill)


