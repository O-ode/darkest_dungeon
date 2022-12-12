from abc import ABC
from typing import Type

from base_classes.basic_attribute import ResistanceBase, OtherAttributeBase
from constants import pretty
from model.character_attributes.base_attributes import BaseLevelAttributesModel
from model.skill.base_skill import BaseSkill


class CharacterModel(ABC):
    
    def __init__(self, name=None):
        self.name: str = name
        self._levels: list[Type[BaseLevelAttributesModel]] = []
        self._resistances: list[Type[ResistanceBase]] = []
        self._other_info: list[Type[OtherAttributeBase]] = []
        self._skills: list[Type[BaseSkill]] = []

    def add_levels_attrs(self, level_level: Type[BaseLevelAttributesModel]):
        self._levels.append(level_level)
        return self

    def add_skill(self, skill: Type[BaseSkill]):
        self._skills.append(skill)
        return self

    def add_resistance(self, resistance: Type[ResistanceBase]):
        self._resistances.append(resistance)
        return self

    def add_other_info(self, other_info: Type[OtherAttributeBase]):
        self._other_info.append(other_info)
        return self

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
