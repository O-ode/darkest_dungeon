import multiprocessing as mp
import warnings
from typing import Generator, Any

from constants import pretty, space_re
from factories.hero_factory import HeroFactory
from model.hero_model import HeroModel
from repos.daos.hero_dao import HeroDAO
from repos.daos.text_reader_daos.constants import HERO_LIST

logger = mp.get_logger()


class HeroesRepo:
    heroes: list[HeroModel] = []

    @classmethod
    def get_heroes(cls) -> Generator[HeroModel, Any, None]:
        if len(cls.heroes) == 0:
            for name in iter(HERO_LIST):
                hero = HeroModel(HeroFactory) \
                    .set_name(name)
                cls.heroes.append(hero)
                yield hero

    @classmethod
    def add_level_attributes_to_hero(cls, hero: HeroModel):
        warnings.warn("Method to be updated", DeprecationWarning)
        pass

    # for attrs in HeroDAO.get_level_attributes(hero):
    #     model = HeroFactory.get_level_attributes_model(**attrs)
    #     logger.info(pretty(model))
    #
    #     hero.add_levels_attrs(model)
    # return cls

    @classmethod
    def get_resistances_from_hero(cls, hero: HeroModel):
        if len(hero.get_resistances()) == 0:
            cls.add_resistances_to_hero(hero)
        return hero.get_resistances()

    @classmethod
    def add_resistances_to_hero(cls, hero: HeroModel):
        for attr_and_value in HeroDAO.get_resistances_for_hero(hero):
            logger.debug(attr_and_value)
            name, value = tuple(space_re.split(attr_and_value))
            resistance = HeroFactory.prepare_resistance(name, value)
            logger.debug(pretty(resistance))
            hero.add_resistance(resistance)
        return cls

    @classmethod
    def get_combat_skills_from_hero(cls, hero: HeroModel):
        if len(hero.get_combat_skills()) == 0:
            cls.add_combat_skills_to_hero(hero)
        return hero.get_resistances()

    @classmethod
    def add_combat_skills_to_hero(cls, hero: HeroModel):
        for attr_and_value in HeroDAO.get_combat_skills(hero):
            skill = HeroFactory.prepare_combat_skill(attr_and_value)
            logger.info(f'{pretty(skill)}')
            hero.add_combat_skill(skill)
        return cls

    @classmethod
    def add_camping_skills_to_hero(cls, hero: HeroModel):
        warnings.warn("Method to be updated", DeprecationWarning)
        for skill_attrs in HeroDAO.get_camping_skills(hero):
            skill = HeroFactory.get_camping_skill(**skill_attrs)
            logger.info(f'{pretty(skill)}')
            hero.add_camping_skill(skill)
        return cls
