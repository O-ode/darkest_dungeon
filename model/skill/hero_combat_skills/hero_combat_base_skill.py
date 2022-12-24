from abc import ABC
from typing import Any

from base_classes.common import Name
from base_classes.skill_attributes import Effect, Limit, Launch, Target, Level
from constants import SkillBooleans
from factories.hero_skill_factories import HeroSkillFactory


class HeroCombatBaseSkill(ABC):

    def __init__(self, factory: HeroSkillFactory):
        self._factory: HeroSkillFactory = factory
        self._name: Name or None = None
        self._level: Level or None = None
        self._launch: Launch or None = None
        self._target: Target or None = None
        self._limit: Limit or None = None
        self._skill_booleans: SkillBooleans or None = None

        self._effects: list[Effect] = []

    def set_name(self, value: Any):
        self._name = self._factory.prepare_skill_name(value)

    def set_level(self, value: Any):
        self._level = self._factory.prepare_level(value)

    def set_launch(self, value: Any):
        self._launch = self._factory.prepare_launch(value)

    def set_target(self, value: Any):
        self._target = self._factory.prepare_target(value)

    def set_limit(self, value: Any):
        self._limit = self._factory.prepare_limit(value)

    def set_skill_booleans(self, **kwargs):
        self._skill_booleans = self._factory.prepare_skill_booleans(**kwargs)

    def add_effect(self, effect: Effect):
        self._effects.append(effect)

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
