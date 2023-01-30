import multiprocessing as mp
from typing import Generator, Any, Type

from builders.character_builder import CharacterBuilder
from composites.hero_composite import HeroComposite
from repos.daos.text_reader_daos.constants import HERO_LIST

logger = mp.get_logger()


class HeroesRepo:
    heroes: list[HeroComposite] = []

    @classmethod
    def get_heroes(cls) -> Generator[HeroComposite, Any, None]:
        if len(cls.heroes) == 0:
            logger.info(f'Generating all heroes by name')
            for name in HERO_LIST:
                builder_class: Type[CharacterBuilder] = eval(name + 'Builder')
                hero = builder_class().build()
                cls.heroes.append(hero)
                yield hero
        else:
            yield from cls.heroes
