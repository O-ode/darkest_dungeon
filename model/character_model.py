from pprint import pformat

from model.character_level_model import CharacterLevelModel
from model.skill_model import SkillModel


class CharacterModel:
    def __init__(self, name=None, bleed=None, blight=None, debuff=None, death_blow=None,
                 disease=None, move=None, stun=None, trap=None, movement=None, crit_buff_bonus=None,
                 religious=None, provisions=None, skills=None, stats=None):
        self.name: str = name
        self.bleed: float = bleed
        self.blight: float = blight
        self.debuff: float = debuff
        self.death_blow: float = death_blow
        self.disease: float = disease
        self.move: float = move
        self.stun: float = stun
        self.trap: float = trap
        self.movement: str = movement
        self.crit_buff_bonus: str = crit_buff_bonus
        self.religious: str = religious
        self.provisions: str = provisions
        self.skills: [SkillModel] = skills
        self.stats: [CharacterLevelModel] = stats

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

    def __str__(self):
        return pformat(self.__dict__)

    def __repr__(self):
        return pformat(self.__dict__)
