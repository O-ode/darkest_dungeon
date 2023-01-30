from typing import Any

from base_classes.skill_attributes import Move
from constants import SkillTypeEnum, pretty
from factories.hero_skill_factories import HeroSkillFactory


class MoveSkill:

    def __init__(self, factory):
        self._factory: HeroSkillFactory = factory
        self._move: Move or None = None
        self._skill_type: SkillTypeEnum or None = None

    def set_move(self, values: list[Any]):
        self._move = self._factory.prepare_move(values)
        return self

    def set_skill_type(self, value: Any):
        self._skill_type = self._factory.prepare_skill_type(value)
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}: {pretty(vars(self))}'
