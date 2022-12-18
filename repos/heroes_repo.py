import logging
from typing import Generator, Any

from constants import pretty
from factories.hero_factory import HeroFactory
from model.hero_model import HeroModel
from repos.daos.hero_dao import HeroDAO
from repos.daos.heroes_dao import HeroesDAO

logger = logging.getLogger()


class HeroesRepo:
    heroes: list[HeroModel] = []

    @classmethod
    def get_heroes(cls) -> Generator[HeroModel, Any, None]:
        if len(cls.heroes) == 0:
            for name in HeroesDAO.get_heroes_names():
                hero = HeroModel(name)
                cls.heroes.append(hero)
                yield hero
        else:
            for hero in cls.heroes:
                logger.info(f'Hero: {hero.name}')
                yield hero

    @classmethod
    def add_level_attributes_to_hero(cls, hero: HeroModel):
        for attrs in HeroDAO.get_level_attributes(hero):
            model = HeroFactory.get_level_attributes_model(**attrs)
            logger.info(pretty(model))

            hero.add_levels_attrs(model)
        return cls

    @classmethod
    def add_resistances_to_hero(cls, hero: HeroModel):
        for attrs in HeroDAO.get_resistances(hero):
            resistance = HeroFactory.get_resistances_attributes(**attrs)
            logger.info(pretty(resistance))
            hero.add_resistance(resistance)
        return cls

    @classmethod
    def add_other_info_to_hero(cls, hero: HeroModel):
        for attrs in HeroDAO.get_other_info(hero):
            other_info = HeroFactory.get_other_info(**attrs)
            logger.info(pretty(other_info))
            hero.add_other_info(other_info)
        return cls

    @classmethod
    def add_skills_to_hero(cls, hero: HeroModel):
        for skill_attrs in HeroDAO.get_skills(hero):
            skill = HeroFactory.get_skill(skill_attrs)
            logger.info(f'{pretty(skill)}')
            hero.add_skill(skill)
        return cls

    @classmethod
    def add_camping_skills_to_hero(cls, hero: HeroModel):
        for skill_attrs in HeroDAO.get_camping_skills(hero):
            skill = HeroFactory.get_camping_skill(**skill_attrs)
            logger.info(f'{pretty(skill)}')
            hero.add_camping_skill(skill)
        return cls
