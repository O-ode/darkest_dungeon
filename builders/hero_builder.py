import multiprocessing as mp
import warnings

from base_classes.basic_attribute import Name
from builders.character_builder import CharacterBuilder
from composites.hero_composite import HeroComposite
from constants import pretty
from factories.hero_factory import HeroFactory
from repos.daos.hero_dao import HeroDAO

logger = mp.get_logger()


# hero_class_map = {'Abomination': Abomination, 'Antiquarian': Antiquarian, 'Arbalest': Arbalest,
#                   'BountyHunter': BountyHunter, 'Crusader': Crusader, 'GraveRobber': GraveRobber, 'Hellion': Hellion,
#                   'Highwayman': Highwayman, 'Houndmaster': Houndmaster, 'Jester': Jester, 'Leper': Leper,
#                   'ManAtArms': ManAtArms, 'Occultist': Occultist, 'PlagueDoctor': PlagueDoctor, 'Vestal': Vestal,
#                   'Flagellant': Flagellant}


class HeroBuilder(CharacterBuilder):

    def __init__(self, name: Name or str):
        if type(name) is Name:
            name = name.value
        # self._character_class = hero_class_map[name]
        self._character_class = eval(name)
        self._dao_interface = HeroDAO

    def build(self):
        hero = self._character_class()
        self.add_resistances(hero) \
            .add_crit_effects(hero) \
            .add_stats(hero) \
            .add_combat_skills(hero) \
            .add_combat_move_skill(hero) \
            .add_tags(hero) \
            .add_deaths_door_effects(hero) \
            .add_generation_conditions(hero)
        return hero

    def add_camping_skills(self, hero: HeroComposite):
        warnings.warn("Method to be updated", DeprecationWarning)
        logger.info(f'Adding camping skills to hero: {hero.get_name()}')
        for skill_attrs in self._dao_interface.get_camping_skills(hero):
            skill = HeroFactory.get_camping_skill(**skill_attrs)
            logger.info(f'{pretty(skill)}')
            hero.add_camping_skill(skill)
        return self

    def add_combat_move_skill(self, hero: HeroComposite):
        logger.info(f'Adding combat move skill to hero: {hero.get_name()}')
        skill_attrs = self._dao_interface.get_combat_move_skill(hero)
        hero.set_combat_move_skill(**skill_attrs)
        return self

    def add_crit_effects(self, hero: HeroComposite):
        logger.info(f'Adding crit effects to hero: {hero.get_name()}')
        crit_attrs = self._dao_interface.get_crit_effects(hero)
        for v in crit_attrs.values():
            # crit_effect = HeroFactory.prepare_crit_effect(v)
            # logger.info(f'{pretty(crit_effect)}')
            hero.add_crit_effect(v)
        return self

    def add_deaths_door_effects(self, hero: HeroComposite):
        logger.info(f'Adding death\'s door effects to hero: {hero.get_name()}')
        hero.set_deaths_door_effect(self._dao_interface.get_deaths_door_effects(hero))
        return self

    def add_generation_conditions(self, hero: HeroComposite):
        logger.info(f'Adding generation conditions to hero: {hero.get_name()}')
        for name, value in self._dao_interface.get_generation_conditions(hero):
            # condition = HeroFactory.prepare_generation_condition(name, value)
            # logger.debug(pretty(condition))
            hero.add_generation_condition(name, value)
        return self
