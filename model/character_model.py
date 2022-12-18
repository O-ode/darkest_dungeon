from abc import ABC

from base_classes.type_vars import DerivedFromBasicAttributes, DerivedFromResistanceBase, DerivedFromOtherAttributeBase
from constants import pretty
from model.skill.type_vars import DerivedFromBaseSkill


class CharacterModel(ABC):

    def __init__(self, name=None):
        self.name: str = name
        self._levels: list[DerivedFromBasicAttributes] = []
        self._resistances: list[DerivedFromResistanceBase] = []
        self._skills: list[DerivedFromBaseSkill] = []
        self._other_info: list[DerivedFromOtherAttributeBase] = []

    def add_levels_attrs(self, level: DerivedFromBasicAttributes):
        self._levels.append(level)
        return self

    def add_other_info(self, other_info: DerivedFromOtherAttributeBase):
        self._other_info.append(other_info)
        return self

    def add_resistance(self, resistance: DerivedFromResistanceBase):
        self._resistances.append(resistance)
        return self

    def add_skill(self, skill: DerivedFromBaseSkill):
        self._skills.append(skill)
        return self

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
