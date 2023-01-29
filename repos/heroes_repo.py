import multiprocessing as mp
import warnings
from typing import Generator, Any

from constants import pretty
from factories.hero_factory import HeroFactory
from model.hero_composites import hero_class_map
from model.hero_model import HeroComposite
from repos.daos.hero_dao import HeroDAO
from repos.daos.text_reader_daos.constants import HERO_LIST

logger = mp.get_logger()


class HeroesRepo:
    heroes: list[HeroComposite] = []

    # @classmethod
    # def add_armors_to_hero(cls, hero: HeroComposite):
    #     logger.info(f'Adding armors to hero: {hero.get_name()}')
    #     for armor_attrs in HeroDAO.get_armors(hero):
    #         armor = HeroFactory.prepare_armor(**armor_attrs)
    #         logger.info(f'{pretty(armor)}')
    #         hero.add_armor(armor)
    #     return cls

    @classmethod
    def add_camping_skills_to_hero(cls, hero: HeroComposite):
        warnings.warn("Method to be updated", DeprecationWarning)
        logger.info(f'Adding camping skills to hero: {hero.get_name()}')
        for skill_attrs in HeroDAO.get_camping_skills(hero):
            skill = HeroFactory.get_camping_skill(**skill_attrs)
            logger.info(f'{pretty(skill)}')
            hero.add_camping_skill(skill)
        return cls

    @classmethod
    def add_combat_move_skill_to_hero(cls, hero: HeroComposite):
        warnings.warn("Method to be updated", DeprecationWarning)
        logger.info(f'Adding combat move skill to hero: {hero.get_name()}')
        skill_attrs = HeroDAO.get_combat_move_skill(hero)
        hero.set_combat_move_skill(**skill_attrs)
        return cls

    @classmethod
    def add_combat_skills_to_hero(cls, hero: HeroComposite):
        logger.info(f'Adding combat skills to hero: {hero.get_name()}')
        for skill_attrs in HeroDAO.get_combat_skills(hero):
            logger.debug(skill_attrs)
            # skill = HeroFactory.prepare_combat_skill(skill_attrs)
            # logger.info(f'{pretty(skill)}')
            hero.add_combat_skill(**skill_attrs)
        return cls

    @classmethod
    def add_crit_effects_to_hero(cls, hero: HeroComposite):
        warnings.warn("Method to be updated", DeprecationWarning)
        logger.info(f'Adding crit effects to hero: {hero.get_name()}')
        crit_attrs = HeroDAO.get_crit_effects(hero)
        for v in crit_attrs.values():
            # crit_effect = HeroFactory.prepare_crit_effect(v)
            # logger.info(f'{pretty(crit_effect)}')
            hero.add_crit_effect(v)
        return cls

    @classmethod
    def add_deaths_door_effects_to_hero(cls, hero: HeroComposite):
        warnings.warn("Method to be updated", DeprecationWarning)
        logger.info(f'Adding death\'s door effects to hero: {hero.get_name()}')
        deaths_door_attrs = HeroDAO.get_deaths_door_effects(hero)
        for v in deaths_door_attrs.values():
            hero.add_deaths_door_effect(v)
        return cls

    @classmethod
    def add_generation_conditions_to_hero(cls, hero: HeroComposite):
        logger.info(f'Adding generation conditions to hero: {hero.get_name()}')
        for name, value in HeroDAO.get_generation_conditions(hero):
            # condition = HeroFactory.prepare_generation_condition(name, value)
            # logger.debug(pretty(condition))
            hero.add_generation_condition(name, value)
        return cls

    @classmethod
    def add_resistances_to_hero(cls, hero: HeroComposite):
        # logger.info(f'Adding resistances to hero: {hero.get_name()}')
        for name, value in HeroDAO.get_resistances(hero):
            # resistance = HeroFactory.prepare_resistance(name, value)
            # logger.debug(pretty(resistance))
            hero.add_resistance(name, value)

        logger.info(f'Resistances added to hero: {pretty(hero.get_resistances())}')
        return cls

    @classmethod
    def add_tags_to_hero(cls, hero: HeroComposite):
        logger.info(f'Adding tags to hero: {hero.get_name()}')
        warnings.warn("Method to be updated", DeprecationWarning)
        for tag_attrs in HeroDAO.get_tags(hero):
            logger.debug(pretty(tag_attrs))
            # tag = HeroFactory.prepare_tag(tag_attrs['id'])
            # logger.debug(pretty(tag))
            hero.add_tag(tag_attrs['id'])
        return cls

    @classmethod
    def add_stats_to_hero(cls, hero: HeroComposite):
        logger.info(f'Adding stats to hero: {hero.get_name()}')
        for stats_attrs in HeroDAO.get_stats(hero):
            logger.debug(pretty(stats_attrs))
            hero.add_stats(**stats_attrs)
        return cls

    @classmethod
    def add_quirk_modifers_to_hero(cls, hero: HeroComposite):
        warnings.warn(f'Method to be updated')
        raise NotImplementedError('lel')
        # logger.info(f'Adding quirk modifers to hero: {hero.get_name()}')
        # for quirk_attrs in HeroDAO.get_quirk_attrs(hero):
        #     pass
        # return cls

    # @classmethod
    # def add_weapons_to_hero(cls, hero: HeroComposite):
    #     logger.info(f'Adding weapons to hero: {hero.get_name()}')
    #     for wpn_attrs in HeroDAO.get_weapons(hero):
    #         # weapon = HeroFactory.prepare_weapon(**wpn_attrs)
    #         # logger.info(f'{pretty(weapon)}')
    #         hero.add_weapon(weapon)
    #     return cls
    #
    # @classmethod
    # def get_armors_from_hero(cls, hero: HeroComposite):
    #     if len(hero.get_armors()) == 0:
    #         cls.add_armors_to_hero(hero)
    #     return hero.get_armors()

    @classmethod
    def get_combat_skills_from_hero(cls, hero: HeroComposite):
        if len(hero.get_combat_skills()) == 0:
            cls.add_combat_skills_to_hero(hero)
        return hero.get_resistances()

    @classmethod
    def get_generation_conditions_from_hero(cls, hero: HeroComposite):
        if len(hero.get_generation_conditions()) == 0:
            cls.add_generation_conditions_to_hero(hero)
        return hero.get_generation_conditions()

    @classmethod
    def get_heroes(cls) -> Generator[HeroComposite, Any, None]:
        if len(cls.heroes) == 0:
            logger.info(f'Generating all heroes by name')
            for name in HERO_LIST:
                hero_class = hero_class_map[name]
                hero = hero_class(HeroFactory) \
                    .set_name(name)
                cls.heroes.append(hero)
                yield hero
        else:
            yield from cls.heroes

    @classmethod
    def get_resistances_from_hero(cls, hero: HeroComposite):
        if len(hero.get_resistances()) == 0:
            cls.add_resistances_to_hero(hero)
        return hero.get_resistances()

    @classmethod
    def get_stats_from_hero(cls, hero: HeroComposite):
        if len(hero.get_stats()) == 0:
            cls.add_resistances_to_hero(hero)
        return hero.get_resistances()

    @classmethod
    def get_quirk_modifiers(cls, hero: HeroComposite):
        if len(hero.get_quirk_modifiers()) == 0:
            cls.add_quirk_modifers_to_hero(hero)
        return hero.get_quirk_modifiers()

    # @classmethod
    # def get_weapons_from_hero(cls, hero: HeroComposite):
    #     if len(hero.get_weapons()) == 0:
    #         cls.add_weapons_to_hero(hero)
    #     return hero.get_weapons()
