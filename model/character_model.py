from abc import ABC, abstractmethod
from typing import Type, Any

from base_classes.character_attributes import Tag
from base_classes.basic_attribute import Name
from base_classes.type_vars import ResistanceType, StatsType, CombatSkillType
from constants import pretty
from factories.type_vars import CharacterFactories


class CharacterComposite(ABC):

    def __init__(self, factory: Type[CharacterFactories]):
        # Single valued base attributes
        self._factory: Type[CharacterFactories] = factory
        self._class_name: Name or None = None

        # Base list attributes
        self._resistances: list[ResistanceType] = []
        self._tags: list[Tag] = []

        # Base list attributes depending on child class
        self._stats: list[StatsType] = []
        self._combat_skills: list[CombatSkillType] = []

    def set_name(self, value: Any):
        self._class_name = self._factory.prepare_name(value)
        return self

    def add_stats(self, **stats_attrs):
        self._stats.append(self._factory.prepare_stats(**stats_attrs))
        return self

    def add_resistance(self, name: str, value: str):
        self._resistances.append(self._factory.prepare_resistance(name, value))
        return self

    def add_combat_skill(self, **skill_attrs):
        self._combat_skills.append(self._factory.prepare_combat_skill(**skill_attrs))
        return self

    def add_tag(self, value: str):
        self._tags.append(self._factory.prepare_tag(value))
        return self

    @abstractmethod
    def get_stats(self) -> list[StatsType]:
        pass

    @abstractmethod
    def get_combat_skills(self) -> list[CombatSkillType]:
        pass

    def get_tags(self) -> list[Tag]:
        return self._tags

    def get_name(self) -> Name:
        return self._class_name

    def get_resistances(self) -> list[ResistanceType]:
        return self._resistances

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
