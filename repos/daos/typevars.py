from typing import Type, TypeVar

from repos.daos.enemy_dao import EnemyDAO
from repos.daos.hero_dao import HeroDAO

DAOType = TypeVar("DAOType", Type[HeroDAO], Type[EnemyDAO])