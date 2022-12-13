from typing import TypeVar
from factories.base_skill_factories import BaseSkillFactory
from factories.hero_skill_factories import HeroSkillFactory

DerivedFromBaseSkillFactory = TypeVar("DerivedFromBaseSkillFactory", BaseSkillFactory, HeroSkillFactory)
