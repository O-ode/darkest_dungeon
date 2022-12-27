from abc import ABC

from base_classes.type_vars import ResistanceType
from constants import pretty
from model.skill.hero_combat_skills.type_vars import HeroCombatSkillTypes


class CharacterModel(ABC):

    def __init__(self, name=None):
        self._name: str = name
        self._resistances: list[ResistanceType] = []
        self._skills: list[HeroCombatSkillTypes] = []

    def add_resistance(self, resistance: ResistanceType):
        self._resistances.append(resistance)
        return self

    def add_skill(self, skill: HeroCombatSkillTypes):
        self._skills.append(skill)
        return self

    def get_name(self):
        return self._name

    def get_resistances(self):
        return self._resistances

    def get_skills(self):
        return self._skills

    def __str__(self):
        return pretty(vars(self))

    def __repr__(self):
        return pretty(vars(self))
