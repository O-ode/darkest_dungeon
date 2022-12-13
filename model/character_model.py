from abc import ABC
from typing import Type

from base_classes.type_vars import DerivedFromBasicAttributes, DerivedFromResistanceBase, DerivedFromOtherAttributeBase
from constants import pretty
from model.skill.type_vars import DerivedFromHeroBaseSkill


class CharacterModel(ABC):

    def __init__(self, name=None):
        self.name: str = name
        self._levels: list[Type[DerivedFromBasicAttributes]] = []
        self._resistances: list[Type[DerivedFromResistanceBase]] = []
        self._other_info: list[Type[DerivedFromOtherAttributeBase]] = []
        self._skills: list[Type[DerivedFromHeroBaseSkill]] = []

    def add_levels_attrs(self, level: Type[DerivedFromBasicAttributes]):
        self._levels.append(level)
        return self

    def add_skill(self, skill: Type[DerivedFromHeroBaseSkill]):
        self._skills.append(skill)
        return self

    def add_resistance(self, resistance: Type[DerivedFromResistanceBase]):
        self._resistances.append(resistance)
        return self

    def add_other_info(self, other_info: Type[DerivedFromOtherAttributeBase]):
        self._other_info.append(other_info)
        return self

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
