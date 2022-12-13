from typing import Any, Type

from base_classes.character_attributes import Crit
from base_classes.skill_attributes import Accuracy, Dmg, Note, Range
from factories.enemy_skill_factories import EnemySkillFactory
from model.skill.base_skill import BaseSkill


class EnemyBaseSkill(BaseSkill):
    def __init__(self, factory: Type[EnemySkillFactory]):
        super(EnemyBaseSkill, self).__init__(factory)
        self._on_range: Range or None = None
        self._notes: list[Note] or None = None

    def set_on_range(self, value: Any):
        self._on_range = self._factory.prepare_on_range(value)

    def set_notes(self, value: Any):
        self._notes = self._factory.prepare_notes(value)

    def get_on_range(self):
        return self._on_range

    def get_notes(self):
        return self._notes


class EnemySupportSkill(EnemyBaseSkill):

    def __init__(self, factory):
        super(EnemySupportSkill, self).__init__(factory)


class EnemyOffensiveSkill(EnemyBaseSkill):

    def __init__(self, factory):
        super(EnemyOffensiveSkill, self).__init__(factory)
        self._dmg: Dmg or None = None
        self._acc: Accuracy or None = None
        self._crit_chance: Crit or None = None

    def set_dmg(self, value: Any):
        self._dmg = self._factory.prepare_dmg(value)

    def set_acc(self, value: Any):
        self._acc = self._factory.prepare_acc(value)

    def set_crit_chance(self, value: Any):
        self._crit_chance = self._factory.prepare_crit_chance(value)

    def get_dmg(self):
        return self._dmg

    def get_acc(self):
        return self._acc

    def get_crit_chance(self):
        return self._crit_chance
