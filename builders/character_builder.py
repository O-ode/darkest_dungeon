import multiprocessing as mp
from abc import ABC, abstractmethod
from typing import Type

from composites.character_composite import CharacterComposite
from constants import pretty
from repos.daos.character_dao import CharacterDAO

logger = mp.get_logger()


class CharacterBuilder(ABC):
    _dao_interface: Type[CharacterDAO]
    _character_class: Type[CharacterComposite]

    @abstractmethod
    def build(self):
        pass

    def add_combat_skills(self, character: CharacterComposite):
        logger.info(f'Adding combat skills to character: {character.get_name()}')
        for skill_attrs in self._dao_interface.get_combat_skills(character):
            logger.debug(skill_attrs)
            character.add_combat_skill(**skill_attrs)
        return self

    def add_resistances(self, character: CharacterComposite):
        # logger.info(f'Adding resistances to character: {character.get_name()}')
        for name, value in self._dao_interface.get_resistances(character):
            # resistance = characterFactory.prepare_resistance(name, value)
            # logger.debug(pretty(resistance))
            character.add_resistance(name, value)

        logger.info(f'Resistances added to character: {pretty(character.get_resistances())}')
        return self

    def add_tags(self, character: CharacterComposite):
        logger.info(f'Adding tags to character: {character.get_name()}')
        for tag_attrs in self._dao_interface.get_tags(character):
            logger.debug(pretty(tag_attrs))
            character.add_tag(tag_attrs['id'])
        return self

    def add_stats(self, character: CharacterComposite):
        logger.info(f'Adding stats to character: {character.get_name()}')
        for stats_attrs in self._dao_interface.get_stats(character):
            logger.debug(pretty(stats_attrs))
            character.add_stats(**stats_attrs)
        return self
