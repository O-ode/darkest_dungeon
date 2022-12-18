from model.character_model import CharacterModel
from model.skill.camping_skill import CampingSkill
from model.skill.type_vars import DerivedFromBaseSkill


class HeroModel(CharacterModel):

    def __init__(self, name=None):
        super(HeroModel, self).__init__(name)
        self._camping_skills: list[CampingSkill] = []

    def add_camping_skill(self, skill: DerivedFromBaseSkill):
        self._camping_skills.append(skill)
        return self
