import multiprocessing as mp
import warnings

from model.hero_model import HeroModel
from repos.daos.text_reader_daos.constants import HERO_FILES
from repos.file_repo import FileRepo

logger = mp.get_logger()


class HeroDAO:
    @classmethod
    def get_resistances_for_hero(cls, hero: HeroModel):
        relative_path, file_name = HERO_FILES[hero.get_name()]
        for attrs_and_values in FileRepo.get_file_values_by_key('resistances', relative_path, file_name):
            for attr_and_value in attrs_and_values:
                yield attr_and_value

    @classmethod
    def get_combat_skills(cls, hero: HeroModel):
        relative_path, file_name = HERO_FILES[hero.get_name()]
        return FileRepo.get_file_values_by_key('combat_skill', relative_path, file_name)

    @classmethod
    def get_weapons(cls, hero: HeroModel):
        relative_path, file_name = HERO_FILES[hero.get_name()]
        return FileRepo.get_file_values_by_key('weapon', relative_path, file_name)

    @classmethod
    def get_armors(cls, hero: HeroModel):
        relative_path, file_name = HERO_FILES[hero.get_name()]
        return FileRepo.get_file_values_by_key('armour', relative_path, file_name)

    @classmethod
    def get_camping_skills(cls, hero):
        warnings.warn("Method to be updated", DeprecationWarning)
        pass
