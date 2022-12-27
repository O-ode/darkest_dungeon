import multiprocessing as mp
import warnings
from typing import Generator, Any

from constants import pretty
from factories.enemy_factory import EnemyFactory
from model.enemy_model import EnemyModel
from repos.daos.enemy_dao import EnemyDAO

warnings.warn("File to be updated", DeprecationWarning)
logger = mp.get_logger()


class EnamiesRepo:
    enemies: list[EnemyModel] = []

    @classmethod
    def get_enemies_and_regions(cls) -> Generator[EnemyModel, Any, None]:
        pass

    @classmethod
    def add_resistances_to_enemy(cls, enemy: EnemyModel):
        for attrs in EnemyDAO.get_resistances(enemy):
            resistance = EnemyFactory.prepare_resistance(**attrs)
            logger.info(pretty(resistance))
            enemy.add_resistance(resistance)
        return cls

    @classmethod
    def add_skills_to_enemy(cls, enemy: EnemyModel):
        for skill_attrs in EnemyDAO.get_skills(enemy):
            skill = EnemyFactory.get_skill(skill_attrs)
            logger.info(f'{pretty(skill)}')
            enemy.add_skill(skill)
        return cls
