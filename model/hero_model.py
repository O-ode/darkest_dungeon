from constants import pretty
from factories.hero_level_attributes import HeroResolveAttributesModel
from factories.other_attributes import OtherHeroAttributes
from factories.resistance_attributes import HeroResistanceModel
from model.skill_model import SkillModel


class HeroModel:
    def __init__(self, name=None):
        self.name: str = name
        self.resolve_levels: {int: HeroResolveAttributesModel} = {}
        self.resistances: HeroResistanceModel or None = None
        self.other_info: OtherHeroAttributes or None = None
        self.skills: [SkillModel] = []

    def add_resolve_levels_attrs(self, resolve_level_dict: {int: HeroResolveAttributesModel}):
        self.resolve_levels.update(resolve_level_dict)
        return self

    def add_skill(self, skill):
        self.skills.append(skill)
        return self

    def add_skills(self, skills):
        self.skills = skills
        return self

    def add_resistances(self, resistances: HeroResistanceModel):
        self.resistances = resistances
        return self

    def add_other_info(self, other_info):
        self.other_info = other_info
        return self

    def __repr__(self):
        return f'{pretty(self.__dict__)}'
