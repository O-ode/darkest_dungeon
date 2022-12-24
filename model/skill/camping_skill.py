from typing import Type, Any

from base_classes.common import Name
from base_classes.skill_attributes import Target, Effect, TimeCost
from constants import pretty
from factories.hero_skill_factories import CampingSkillFactory


class CampingSkill:
    def __init__(self, factory: Type[CampingSkillFactory]):
        self._factory = factory
        self._skill_name: Name or None = None
        self._time_cost: TimeCost or None = None
        self._target: Target or None = None
        self._description: list[Effect] or None = None

    def set_skill_name(self, value: Any):
        self._skill_name = self._factory.prepare_skill_name(value)
        return self

    def set_time_cost(self, value: Any):
        self._time_cost = self._factory.prepare_time_cost(value)
        return self

    def set_target(self, value: Any):
        self._target = self._factory.prepare_target(value)
        return self

    def set_description(self, value: Any):
        self._description = self._factory.prepare_description(value)
        return self

    def get_skill_name(self):
        return self._skill_name

    def get_time_cost(self):
        return self._time_cost

    def get_target(self):
        return self._target

    def get_description(self):
        return self._description

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
