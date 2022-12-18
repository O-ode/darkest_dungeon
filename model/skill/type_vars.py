from typing import TypeVar

from factories.enemy_attributes_factories import EnemyAttributesFactory
from factories.hero_attributes_factories import HeroLevelAttributesFactory
from model.skill.camping_skill import CampingSkill
from model.skill.enemy_skills import EnemyBaseSkill, EnemySupportSkill, EnemyOffensiveSkill
from model.skill.hero_skills import HeroBaseSkill, HeroOffensiveSkill, HeroSupportSkill, HeroHealSkill

DerivedFromBaseSkill = TypeVar("DerivedFromBaseSkill", HeroBaseSkill, HeroOffensiveSkill,
                               HeroSupportSkill, HeroHealSkill, EnemyBaseSkill, EnemySupportSkill,
                               EnemyOffensiveSkill, CampingSkill)

CharacterModelFactories = TypeVar("CharacterModelFactories", HeroLevelAttributesFactory, EnemyAttributesFactory)