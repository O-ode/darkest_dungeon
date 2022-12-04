from model.character_stat_model import CharacterStatModel
from model.other_information_model import OtherInformationModel
from model.resistance_stat_model import ResistanceStatModel
from model.skill_model import SkillModel


class CharacterModel:
    def __init__(self, name=None, skills=None, stats=None, resistances=None, other_info=None):
        self.name: str = name
        self.resistances: ResistanceStatModel = resistances
        self.stats: [CharacterStatModel] = stats
        self.other_info: OtherInformationModel = other_info
        self.skills: [SkillModel] = skills

    def add_stat(self, stat):
        self.stats.append(stat)
        return self

    def add_stats(self, stats):
        self.stats = stats
        return self

    def add_skill(self, skill):
        self.skills.append(skill)
        return self

    def add_skills(self, skills):
        self.skills = skills
        return self

    def add_resistances(self, resistances):
        self.resistances = resistances
        return self

    def add_other_info(self, other_info):
        self.other_info = other_info
        return self

    def __str__(self):
        keyorder = ['name', 'resistances', 'stats', 'other_info', 'skills']
        dic = {k: self.__dict__[k] for k in keyorder if k in self.__dict__}
        return repr(dic)

    def __repr__(self):
        keyorder = ['name', 'resistances', 'stats', 'other_info', 'skills']
        dic = {k: self.__dict__[k] for k in keyorder if k in self.__dict__}
        return repr(dic)
