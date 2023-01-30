import datetime
import multiprocessing as mp
import os.path

from graphics.hero_charts import HeroArtist
from repos.heroes_repo import HeroesRepo


def setup_logger():
    import logging
    _logger = mp.get_logger()
    formatter = logging.Formatter("[%(asctime)s:%(levelname)7s:%(filename)s:%(lineno)s:%(funcName)s()] %(message)s")

    file_handler = logging.FileHandler(os.path.join(os.getcwd(),
                                                    f'log_{datetime.datetime.now().strftime("%d_%b_%Y_%H_%M_%S")}.log'),
                                       encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    _logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    _logger.addHandler(console_handler)
    _logger.setLevel(logging.DEBUG)
    return _logger


if __name__ == '__main__':
    logger = setup_logger()
    for i, hero in enumerate(HeroesRepo.get_heroes(), start=1):
        logger.info(f'Hero nª {i}: {hero}')
        # HeroesRepo.add_resistances_to_hero(hero) \
        #     .add_crit_effects_to_hero(hero) \
        #     .add_stats_to_hero(hero) \
        #     .add_combat_skills_to_hero(hero) \
        #     .add_combat_move_skill_to_hero(hero) \
        #     .add_tags_to_hero(hero) \
        #     .add_deaths_door_effects_to_hero(hero) \
        #     .add_generation_conditions_to_hero(hero)

        # HeroesRepo.add_camping_skills_to_hero(hero)

    HeroArtist.display_hero_attr_comparison([hero for hero in HeroesRepo.get_heroes()])

    exit(0)
