import logging

from factories.hero_level_attributes import HeroResolveAttributesModel, HeroResolveAttributesFactory
from factories.other_attributes import OtherHeroAttributes, OtherHeroAttributesFactory
from factories.resistance_attributes import ResistancesFactory, HeroResistanceModel
from model.hero_model import HeroModel
from repos.daos.hero_dao import HeroDAO
from repos.daos.heroes_dao import HeroesDAO

logger = logging.getLogger()
class HeroesRepo:
    heroes: [HeroModel] = []

    @classmethod
    def get_heroes(cls):
        if len(cls.heroes) == 0:
            for name in HeroesDAO.get_heroes_names():
                hero = HeroModel(name)
                cls.heroes.append(hero)
            yield from cls.heroes
        else:
            for hero in cls.heroes:
                yield hero

    @classmethod
    def add_resolve_level_attributes_to_hero(cls, hero: HeroModel):
        for level, attrs in HeroDAO.get_transformed_resolve_level_attributes(hero):
            model = HeroResolveAttributesModel(HeroResolveAttributesFactory).set_values(**attrs)
            hero.add_resolve_levels_attrs({level: model})
        logger.info(hero)
        return cls

    @classmethod
    def add_resistances_to_hero(cls, hero: HeroModel):
        resistances_model = HeroResistanceModel(ResistancesFactory)
        resistances = {name: value for name, value in HeroDAO.get_resistances(hero)}
        resistances_model.set_values(**resistances)
        hero.add_resistances(resistances_model)
        return cls

    @classmethod
    def add_other_info_to_hero(cls, hero: HeroModel):
        other_info = OtherHeroAttributes(OtherHeroAttributesFactory)
        other_info_kwargs = {name: value for name, value in HeroDAO.get_other_info(hero)}
        other_info.set_values(**other_info_kwargs)
        hero.add_other_info(other_info)
        return cls
