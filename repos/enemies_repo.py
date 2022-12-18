import logging
from typing import Generator, Any

from constants import pretty
from factories.enemy_factory import EnemyFactory
from model.enemy_model import EnemyModel
from repos.daos.enemies_dao import EnemiesDAO
from repos.daos.enemy_dao import EnemyDAO
from repos.regions_repo import RegionsRepo

logger = logging.getLogger()


class EnamiesRepo:
    enemies: list[EnemyModel] = []

    @classmethod
    def get_enemies_and_regions(cls) -> Generator[EnemyModel, Any, None]:
        if len(cls.enemies) == 0:
            for region_name, enemies_names in EnemiesDAO.get_enemies_per_region():
                for name in enemies_names:
                    enemy = EnemyModel(name)
                    cls.enemies.append(enemy)
                    yield enemy
                RegionsRepo.add_region_and_enemy_names(region_name, enemies_names)

        else:
            for enemy in cls.enemies:
                logger.info(f'Enemy: {enemy.name}')
                yield enemy

    @classmethod
    def add_level_attributes_to_enemy(cls, enemy: EnemyModel):
        for attrs in EnemyDAO.get_level_attributes(enemy):
            model = EnemyFactory.get_level_attributes_model(**attrs)
            logger.info(pretty(model))

            enemy.add_levels_attrs(model)
        return cls

    @classmethod
    def add_resistances_to_enemy(cls, enemy: EnemyModel):
        for attrs in EnemyDAO.get_resistances(enemy):
            resistance = EnemyFactory.get_resistances_attributes(**attrs)
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
