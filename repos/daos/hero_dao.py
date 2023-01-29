import multiprocessing as mp
import re

from model.hero_model import HeroComposite
from repos.daos.text_reader_daos.constants import HERO_FILES
from repos.file_repo import FileRepo

logger = mp.get_logger()


class HeroDAO:

    @classmethod
    def get_armors(cls, hero: HeroComposite):
        # logger.info(f'Getting armors for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        for armor_attrs in FileRepo.get_file_values_by_key('armour', relative_path, file_name):
            attr_filter = ['armor_name', 'dodge', 'hp']
            name_alterations = {'def': 'dodge', 'name': 'armor_name'}
            transformed_attrs = {}

            for name, value in armor_attrs.items():
                if name in name_alterations:
                    name = name_alterations[name]
                if name in attr_filter:
                    transformed_attrs[name] = value[0]

            logger.info(transformed_attrs)
            yield transformed_attrs

    @classmethod
    def get_combat_move_skill(cls, hero: HeroComposite):
        # logger.info(f'Getting combat move skill for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        skill_attrs = next(FileRepo.get_file_values_by_key('combat_move_skill', relative_path, file_name))
        list_values = ['move']
        name_alterations = {'type': 'value_type'}
        attr_filter = ['value_type', 'move']

        transformed_attrs = {}
        for name, value in skill_attrs.items():
            if name in name_alterations:
                name = name_alterations[name]
            if name in attr_filter:
                if name not in list_values:
                    value = value[0]
                transformed_attrs[name] = value

        return transformed_attrs

    @classmethod
    def get_combat_skills(cls, hero: HeroComposite):
        # logger.info(f'Getting combat skills for hero: {hero.get_name()}')
        list_values = ['move', 'effect', 'heal']
        merge_into_effects = ['beast_effects', 'human_effects']
        skip = ['valid_modes', 'per_turn_limit', 'self_target_valid']
        skill_boolean_names = ['is_crit_valid', 'is_continue_turn', 'is_stall_invalidating', 'refresh_after_each_wave',
                               'ignore_stealth', 'self_target_valid', 'generation_guaranteed', 'ignore_protection',
                               'ignore_guard']
        name_alterations = {'id': 'value_id', 'type': 'value_type'}
        relative_path, file_name = HERO_FILES[hero.get_name()]
        for skill_attrs in FileRepo.get_file_values_by_key('combat_skill', relative_path, file_name):
            skill_booleans = {}
            transformed_attrs = {}
            for name, value in skill_attrs.items():
                if name in name_alterations:
                    name = name_alterations[name]
                if name in skip:
                    continue
                elif name in skill_boolean_names:
                    if re.search(r'true', value[0]):
                        value = True
                    else:
                        value = False
                    skill_booleans[name] = value
                    continue

                if name in merge_into_effects:
                    name = 'effect'

                if name not in list_values:
                    if len(value) > 0:
                        value = value[0]
                    else:
                        value = ''

                # logger.debug(f'{name} {value}')
                if name in list_values and name in transformed_attrs:
                    transformed_attrs[name].extend(value)
                else:
                    transformed_attrs[name] = value

            transformed_attrs['skill_booleans'] = skill_booleans
            # logger.debug(transformed_attrs)
            yield transformed_attrs

    @classmethod
    def get_crit_effects(cls, hero: HeroComposite):
        # logger.info(f'Getting crit effects for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        crit_attrs = next(FileRepo.get_file_values_by_key('crit', relative_path, file_name))
        return crit_attrs

    @classmethod
    def get_deaths_door_effects(cls, hero: HeroComposite):
        # logger.info(f'Getting death\'s door effects for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        crit_attrs = next(FileRepo.get_file_values_by_key('deaths_door', relative_path, file_name))
        return crit_attrs

    @classmethod
    def get_generation_conditions(cls, hero: HeroComposite):
        # logger.info(f'Getting generation conditions for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        gen_attrs = next(FileRepo.get_file_values_by_key('generation', relative_path, file_name))
        for k, v in gen_attrs.items():
            yield k, v[0]

    @classmethod
    def get_resistances(cls, hero: HeroComposite):
        # logger.info(f'Getting resistances for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        res_dict = next(FileRepo.get_file_values_by_key('resistances', relative_path, file_name))
        for name, value_list in res_dict.items():
            yield name, value_list[0]

    @classmethod
    def get_tags(cls, hero: HeroComposite):
        # logger.info(f'Getting tags for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        for tag_attrs in FileRepo.get_file_values_by_key('tag', relative_path, file_name):
            transformed_attrs = {}
            for k, v in tag_attrs.items():
                transformed_attrs[k] = v[0]
            yield transformed_attrs

    @classmethod
    def get_stats(cls, hero: HeroComposite):
        # logger.info(f'Getting stats for hero: {hero.get_name()}')
        weapons = cls.get_weapons(hero)
        armors = cls.get_armors(hero)
        for i in range(5):
            attrs = [next(weapons), next(armors)]
            logger.info(attrs)
            attrs = {k: v for a in attrs for k, v in a.items()}
            yield attrs

    @classmethod
    def get_weapons(cls, hero: HeroComposite):
        # logger.info(f'Getting weapons for hero: {hero.get_name()}')
        relative_path, file_name = HERO_FILES[hero.get_name()]
        for wpn_attrs in FileRepo.get_file_values_by_key('weapon', relative_path, file_name):
            attr_filter = ['weapon_name', 'dmg', 'crit', 'spd']
            name_alterations = {'name': 'weapon_name'}
            list_values = ['dmg']
            transformed_attrs = {}
            for name, value in wpn_attrs.items():
                if name in name_alterations:
                    name = name_alterations[name]
                if name in attr_filter:
                    if name not in list_values:
                        value = value[0]
                    transformed_attrs[name] = value
            logger.debug(transformed_attrs)
            yield transformed_attrs
