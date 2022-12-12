from abc import ABC
from typing import Type, Any

from base_classes.character_attributes import Level
from base_classes.skill_attributes import Effect, Rank, SkillName, Target
from constants import pretty
from factories.hero_skill_factories import HeroSkillFactory


class BaseSkill(ABC):
    def __init__(self, factory):
        self._factory: Type[HeroSkillFactory] = factory
        self._level: list[Level] or None = None
        self._skill_name: SkillName or None = None
        self._rank: Rank or None = None
        self._target: Target or None = None
        self._on_target: list[list[Effect]] or None = None
        self._on_self: list[list[Effect]] or None = None

    def set_level(self, values: list[Any]):
        self._level = self._factory.prepare_level(value)
        return self

    def set_skill_name(self, value: Any):
        self._skill_name = self._factory.prepare_skill_name(value)
        return self

    def set_rank(self, value: Any):
        self._rank = self._factory.prepare_rank(value)
        return self

    def set_target(self, value: Any):
        self._target = self._factory.prepare_target(value)
        return self

    def set_on_target(self, values: list[Any]):
        self._on_target = self._factory.prepare_on_target(value)
        return self

    def set_on_self(self, values: list[Any]):
        self._on_self = self._factory.prepare_on_self(value)
        return self

    def get_level(self):
        return self._level

    def get_skill_name(self):
        return self._skill_name

    def get_rank(self):
        return self._rank

    def get_target(self):
        return self._target

    def get_on_target(self):
        return self._on_target

    def get_on_self(self):
        return self._on_self

    def __hash__(self):
        return hash(self._skill_name)

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
