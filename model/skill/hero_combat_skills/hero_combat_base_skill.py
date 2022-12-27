from abc import ABC
from typing import Any, Type

from base_classes.common import Name
from base_classes.skill_attributes import Effect, Limit, Launch, Target, Level
from constants import SkillBooleans, pretty
from factories.hero_skill_factories import HeroSkillFactory


class HeroCombatBaseSkill(ABC):

    def __init__(self, factory: Type[HeroSkillFactory]):
        self._factory: Type[HeroSkillFactory] = factory
        self._name: Name or None = None
        self._level: Level or None = None
        self._launch: Launch or None = None
        self._target: Target or None = None
        self._limit: Limit or None = None
        self._skill_booleans: SkillBooleans or None = None

        self._effects: list[Effect] = []

    def set_name(self, value: Any):
        self._name = self._factory.prepare_skill_name(value)
        return self

    def set_level(self, value: Any):
        self._level = self._factory.prepare_level(value)
        return self

    def set_launch(self, value: Any):
        self._launch = self._factory.prepare_launch(value)
        return self

    def set_target(self, value: Any):
        self._target = self._factory.prepare_target(value)
        return self

    def set_limit(self, value: Any):
        self._limit = self._factory.prepare_limit(value)
        return self

    def set_skill_booleans(self, **kwargs):
        self._skill_booleans = self._factory.prepare_skill_booleans(**kwargs)
        return self

    def set_effects(self, effects: list[str]):
        for effect in effects:
            self._effects.append(self._factory.prepare_effect(effect))
        return self

    def add_effect(self, effect: Effect):
        self._effects.append(effect)
        return self

    def get_limit(self):
        return self._limit

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_launch(self):
        return self._launch

    def get_target(self):
        return self._target

    def get_effects(self):
        return self._effects

    def get_skill_booleans(self):
        return self._skill_booleans

    def __repr__(self):
        return pretty(vars(self))
