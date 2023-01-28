import multiprocessing as mp
import warnings
from typing import Callable, Any

from base_classes.hero_attributes import GenerationCondition
from base_classes.hero_stats_composite import HeroStatsComposite
from base_classes.skill_attributes import Effect
from constants import pretty
from factories.abstract_character_composite_factory import AbstractCharacterCompositeFactory
from factories.generation_condition_factory import GenerationConditionFactory
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


class HeroFactory(AbstractCharacterCompositeFactory):

    @classmethod
    def prepare_stats(cls, **stats_attrs) -> HeroStatsComposite:
        stats = HeroStatsComposite().set_armor_name(stats_attrs['armor_name']) \
            .set_weapon_name(stats_attrs['weapon_name']) \
            .set_hp(stats_attrs['hp']) \
            .set_dodge(stats_attrs['dodge']) \
            .set_spd(stats_attrs['spd']) \
            .set_dmg(stats_attrs['dmg']) \
            .set_crit(stats_attrs['crit'])
        logger.info(f'{pretty(stats)}')
        return stats

    @classmethod
    def prepare_combat_move_skill(cls, type: str, move: list[str]) -> MoveSkill:
        skill = MoveSkill(HeroSkillFactory) \
            .set_move(move) \
            .set_skill_type(type)
        logger.info(f'{pretty(skill)}')
        return skill

    @classmethod
    def prepare_combat_skill(cls, **skill_attrs):
        if 'heal' in skill_attrs:
            skill = cls.prepare_healing_skill(**skill_attrs)
        else:
            skill = cls.prepare_offensive_skill(**skill_attrs)
        logger.debug(skill)
        return skill

    @classmethod
    def prepare_crit_effect(cls, value: str):
        return Effect(value)

    @classmethod
    def prepare_deaths_door_effect(cls, value: str):
        return Effect(value)

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
        return Armor(HeroArmorFactory) \
            .set_name(name) \
            .set_hp(hp) \
            .set_dodge(dodge)

    @classmethod
    def prepare_generation_condition(cls, name: str, value: str):
        mapping = {
            'is_generation_enabled': GenerationConditionFactory.prepare_bool_value,
            'town_event_dependency': GenerationConditionFactory.prepare_str_value,
            'number_of_positive_quirks_min': GenerationConditionFactory.prepare_int_value,
            'number_of_positive_quirks_max': GenerationConditionFactory.prepare_int_value,
            'number_of_negative_quirks_min': GenerationConditionFactory.prepare_int_value,
            'number_of_negative_quirks_max': GenerationConditionFactory.prepare_int_value,
            'number_of_class_specific_camping_skills': GenerationConditionFactory.prepare_int_value,
            'number_of_shared_camping_skills': GenerationConditionFactory.prepare_int_value,
            'number_of_random_combat_skills': GenerationConditionFactory.prepare_int_value,
            'number_of_cards_in_deck': GenerationConditionFactory.prepare_int_value,
            'card_chance': GenerationConditionFactory.prepare_float_value
        }
        factory_method: Callable[[str], Any] = mapping[name]
        return GenerationCondition(factory_method) \
            .set_name(name) \
            .set_value(value)

    @classmethod
    def get_camping_skill(cls, skill_name: str, time_cost: str, target: str, description: str):
        warnings.warn("Method to be updated", DeprecationWarning)
        return CampingSkill(CampingSkillFactory) \
            .set_skill_name(skill_name) \
            .set_time_cost(time_cost) \
            .set_target(target) \
            .set_description(description)
