import multiprocessing as mp
import re
import warnings

from base_classes.common import Name
from constants import OpenQuotesEnum
from factories.character_factory import CharacterFactory
from factories.hero_armor_factory import HeroArmorFactory
from factories.hero_camping_skill_factories import CampingSkillFactory
from factories.hero_skill_factories import HeroSkillFactory
from factories.hero_weapon_factory import HeroWeaponFactory
from model.armor_model import Armor
from model.skill.camping_skill import CampingSkill
from model.skill.hero_combat_skills.hero_heal_combat_skill import HeroHealCombatSkill
from model.skill.hero_combat_skills.hero_offensive_combat_skill import HeroOffensiveCombatSkill
from model.skill.move_skill import MoveSkill
from model.weapon_model import Weapon

logger = mp.get_logger()


class HeroFactory(CharacterFactory):

    @classmethod
    def prepare_combat_move_skill(cls, **kwargs) -> MoveSkill:
        warnings.warn("Method to be updated", DeprecationWarning)
        return MoveSkill(HeroSkillFactory) \
            .set_move(kwargs['move']) \
            .set_skill_type(kwargs['type'])

    @classmethod
    def prepare_name(cls, name: str):
        return Name(re.search(r'[\s\w]+', name).group())

    @classmethod
    def prepare_combat_skill(cls, str_attrs: str):
        # logger.debug(pretty(str_attrs))
        list_values = ['move', 'effect', 'heal']
        merge_into_effects = ['beast_effects', 'human_effects']
        skip = ['valid_modes', 'per_turn_limit', 'self_target_valid']
        skill_boolean_names = ['is_crit_valid', 'is_continue_turn', 'is_stall_invalidating', 'refresh_after_each_wave',
                               'ignore_stealth', 'self_target_valid', 'generation_guaranteed', 'ignore_protection',
                               'ignore_guard']
        skill_booleans = {}
        dict_attrs = {}
        names = set()
        for attr in str_attrs:
            buffered = []
            split = []
            flag = OpenQuotesEnum(0)
            for letter in attr:
                if re.match(r'\s', letter) and flag.value == 0:
                    if len(buffered) > 0:
                        split.append(''.join(buffered))
                        buffered = []
                        continue
                elif letter == '\'':
                    flag ^= OpenQuotesEnum.SINGLE
                elif letter == '"':
                    flag ^= OpenQuotesEnum.DOUBLE
                buffered.append(letter)
            if len(buffered) > 0:
                split.append(''.join(buffered))

            name = split[0]
            if name in skip:
                continue
            if name in merge_into_effects:
                name = 'effect'

            if name in list_values:
                if len(split[1:]) == 0:
                    value = []
                else:
                    value = split[1:]
            else:
                if len(split[1:]) == 0:
                    value = ''
                else:
                    value = split[1]

            names.add(name)

            if name in merge_into_effects:
                if len(dict_attrs[name]) > 0:
                    dict_attrs[name].append(value)
                else:
                    dict_attrs[name] = [value]
            elif name in skill_boolean_names:
                if re.search(r'true', value):
                    value = True
                else:
                    value = False
                skill_booleans[name] = value
            else:
                dict_attrs[name] = value
        dict_attrs['skill_booleans'] = skill_booleans

        logger.debug(dict_attrs)
        if 'heal' in dict_attrs:
            skill = cls.prepare_healing_skill(**dict_attrs)
        else:
            skill = cls.prepare_offensive_skill(**dict_attrs)
        return skill

    @classmethod
    def prepare_offensive_skill(cls, id: str, level: str, type: str, atk: str, dmg: str, crit: str, launch: str,
                                target: str, skill_booleans=None, effect=None, per_battle_limit: str = '0', move=None) \
            -> HeroOffensiveCombatSkill:
        if skill_booleans is None:
            skill_booleans = {}
        if effect is None:
            effect = []

        logger.debug('Preparing offensive skill')
        model = HeroOffensiveCombatSkill(HeroSkillFactory).set_name(id) \
            .set_level(level) \
            .set_skill_type(type) \
            .set_acc(atk) \
            .set_dmg_mod(dmg) \
            .set_crit_mod(crit) \
            .set_launch(launch) \
            .set_target(target) \
            .set_skill_booleans(**skill_booleans) \
            .set_limit(per_battle_limit) \
            .set_effects(effect)

        if move:
            model.set_move(move)

        return model

    @classmethod
    def prepare_healing_skill(cls, id: str, level: str, launch: str, heal: list[str], target: str, skill_booleans=None,
                              effect=None, per_battle_limit: str = '0') \
            -> HeroHealCombatSkill:
        if skill_booleans is None:
            skill_booleans = {}
        if effect is None:
            effect = []

        return HeroHealCombatSkill(HeroSkillFactory) \
            .set_name(id).set_level(level) \
            .set_launch(launch) \
            .set_heal(heal) \
            .set_target(target) \
            .set_skill_booleans(**skill_booleans) \
            .set_effects(effect) \
            .set_limit(per_battle_limit)

    @classmethod
    def prepare_weapon(cls, name: str, dmg: list[str], crit: str, spd: str):
        return Weapon(HeroWeaponFactory) \
            .set_name(name) \
            .set_dmg(dmg) \
            .set_crit(crit) \
            .set_spd(spd)

    @classmethod
    def prepare_armor(cls, name: str, hp: str, dodge: str):
        # commented out parameters must stay in method definition
        return Armor(HeroArmorFactory) \
            .set_name(name) \
            .set_hp(hp) \
            .set_dodge(dodge)

    @classmethod
    def get_camping_skill(cls, skill_name: str, time_cost: str, target: str, description: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return CampingSkill(CampingSkillFactory) \
            .set_skill_name(skill_name) \
            .set_time_cost(time_cost) \
            .set_target(target) \
            .set_description(description)
