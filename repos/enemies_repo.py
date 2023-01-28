import multiprocessing as mp
import warnings

from factories.enemy_factory import EnemyFactory
from model.enemy_model import EnemyComposite
from repos.daos.enemy_dao import EnemyDAO

warnings.warn("File to be updated", DeprecationWarning)
logger = mp.get_logger()


class EnemiesRepo:
    enemies: list[EnemyComposite] = []

    @classmethod
    def get_all_enemies(cls):
        if len(cls.enemies) == 0:
            cls.generate_enemies()
        return cls.enemies

    @classmethod
    def generate_enemies(cls):
        if len(cls.enemies) == 0:
            logger.info(f'Generating all heroes by name')
            for name in EnemyDAO.get_all_enemies_names():
                model = EnemyComposite(EnemyFactory).set_name(name)
        return cls.enemies
