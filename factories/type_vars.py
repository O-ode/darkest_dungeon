from typing import TypeVar

from factories.base_skill_factories import BaseSkillFactory
from factories.enemy_factory import EnemyFactory
from factories.hero_factories.flagellant_factory import FlagellantFactory
from factories.hero_factory import HeroFactory
from factories.hero_skill_factories import HeroSkillFactory

DerivedFromBaseSkillFactory = TypeVar("DerivedFromBaseSkillFactory", BaseSkillFactory, HeroSkillFactory)
CharacterFactories = TypeVar("CharacterFactories", HeroFactory, FlagellantFactory, EnemyFactory)
HeroFactoryType = TypeVar("HeroFactoryType", HeroFactory, FlagellantFactory)
