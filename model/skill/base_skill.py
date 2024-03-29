import warnings
from abc import ABC
from typing import Any, Type

from base_classes.basic_attribute import Name
from base_classes.skill_attributes import Effect, Launch, Target, Level
from constants import pretty
from factories.type_vars import DerivedFromBaseSkillFactory

warnings.warn("Deprecated", DeprecationWarning)


class BaseSkill(ABC):
    warnings.warn("Replaced by HeroOffensiveCombatSkill", DeprecationWarning)

    def __init__(self, factory):
        warnings.warn("Replaced by HeroOffensiveCombatSkill", DeprecationWarning)
        self._factory: Type[DerivedFromBaseSkillFactory] = factory
        self._skill_name: Name or None = None
        self._level: Level or None = None
        self._launch: Launch or None = None
        self._target: Target or None = None
        self._on_target: list[list[Effect]] or None = None
        self._on_self: list[list[Effect]] or None = None

    def set_skill_name(self, value: Any):
        warnings.warn("Replaced by HeroOffensiveCombatSkill", DeprecationWarning)
        self._skill_name = self._factory.prepare_skill_name(value)
        return self

    def set_resolve_level(self, value: Any):
        self._level = self._factory.prepare_level(value)
        return self

    def set_launch(self, value: Any):
        self._launch = self._factory.prepare_launch(value)
        return self

    def set_target(self, value: Any):
        self._target = self._factory.prepare_target(value)
        return self

    def set_on_target(self, values: list[Any]):
        self._on_target = self._factory.prepare_on_target(values)
        return self

    def set_on_self(self, values: list[Any]):
        self._on_self = self._factory.prepare_on_self(values)
        return self

    def get_skill_name(self):
        return self._skill_name

    def get_launch(self):
        return self._launch

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
