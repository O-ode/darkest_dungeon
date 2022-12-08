import logging
import re

from model.hero_model import HeroModel
from model.skill_model import SkillModel

logger = logging.getLogger()


def get_characters_with_effects(_characters: [HeroModel], patterns: [re.Pattern]):
    for pattern in patterns:
        yield get_characters_with_effect(_characters, pattern)


def get_characters_with_effect(_characters: [HeroModel], pattern: re.Pattern):
    def _get_skills_with_effect(_skills: [SkillModel], _pattern: re.Pattern):
        for skill in iter(_skills):
            for effect in iter(skill.effects):
                if _pattern.search(effect.description):
                    yield skill

    for character in iter(_characters):
        skills = [skill for skill in _get_skills_with_effect(character.skills, pattern)]
        if len(skills) > 0:
            yield HeroModel(character.class_name, skills)


