from factories.hero_attributes_factories import HerolevelAttributesFactory, ResistancesFactory, \
    OtherHeroAttributesFactory
from factories.hero_skill_factories import HeroSkillFactory
from model.character_attributes.hero_attributes import HerolevelAttributesModel
from model.skill.hero_skills import HeroSupportSkill, HeroHealSkill, HeroOffensiveSkill


class CharacterManager:

    @classmethod
    def get_skill(cls, attrs: dict):
        if 'dmg_mod' in attrs['leveled_attributes'][0].keys():
            skill = cls._get_offensive_skill(**attrs)
        elif 'heal' in attrs['leveled_attributes'][0].keys():
            skill = cls._get_healing_skill(**attrs)
        else:
            skill = cls._get_support_skill(**attrs)
        return skill

    @classmethod
    def _get_support_skill(cls, skill_name: str, rank: list[int], target: list[int],
                           on_target: str, on_self: str, on_other_heroes: str, limit: str) \
            -> HeroSupportSkill:
        return HeroSupportSkill(HeroSkillFactory) \
            .set_skill_name(skill_name) \
            .set_rank(rank)\
            .set_target(target) \
            .set_on_target(on_target)\
            .set_on_self(on_self) \
            .set_on_other_heroes(on_other_heroes) \
            .set_limit(limit)

    @classmethod
    def _get_healing_skill(cls, skill_name: str, rank: list[int], target: list[int],
                           on_target: str, on_self: str, on_other_heroes: str, limit: str, heal: str) \
            -> HeroHealSkill:
        return HeroHealSkill(HeroSkillFactory) \
            .set_skill_name(skill_name) \
            .set_rank(rank)\
            .set_target(target) \
            .set_on_target(on_target)\
            .set_on_self(on_self) \
            .set_on_other_heroes(on_other_heroes) \
            .set_limit(limit) \
            .set_heal(heal)

    @classmethod
    def _get_offensive_skill(cls, skill_name: str, rank: list[int], target: list[int],
                             limit: str, leveled_attributes: list[dict]) \
            -> HeroOffensiveSkill:
        return HeroOffensiveSkill(HeroSkillFactory) \
            .set_skill_name(skill_name) \
            .set_rank(rank)\
            .set_target(target)\
            .set_limit(limit)

    @classmethod
    def _get_offensive_skill(cls, skill_name: str, rank: list[int], target: list[int], on_target: str, on_self: str,
                             on_other_heroes: str, limit: str, on_range: str, dmg_mod: str, acc: str, crit_mod: str) \
            -> HeroOffensiveSkill:
        return HeroOffensiveSkill(HeroSkillFactory) \
            .set_skill_name(skill_name) \
            .set_rank(rank)\
            .set_target(target) \
            .set_on_target(on_target)\
            .set_on_self(on_self) \
            .set_on_other_heroes(on_other_heroes) \
            .set_limit(limit) \
            .set_on_range(on_range) \
            .set_dmg_mod(dmg_mod) \
            .set_acc(acc) \
            .set_crit_mod(crit_mod)

    @classmethod
    def get_hero_level_attributes_model(cls, resolve: str, max_hp: str, dodge: str, prot: str,
                                        spd: str, acc_mod: str, crit: str, dmg: str) \
            -> HerolevelAttributesModel:
        return HerolevelAttributesModel(HerolevelAttributesFactory) \
            .set_level(resolve) \
            .set_hp(max_hp) \
            .set_dodge(dodge) \
            .set_prot(prot) \
            .set_spd(spd) \
            .set_acc_mod(acc_mod) \
            .set_crit(crit) \
            .set_dmg(dmg)

    @classmethod
    def get_resistances_attributes(cls, name: str, value: str):
        resistances_dict = {
            "stun": ResistancesFactory.prepare_stun,
            "move": ResistancesFactory.prepare_move,
            "blight": ResistancesFactory.prepare_blight,
            "bleed": ResistancesFactory.prepare_bleed,
            "disease": ResistancesFactory.prepare_disease,
            "debuff": ResistancesFactory.prepare_debuff,
            "death_blow": ResistancesFactory.prepare_death_blow,
            "trap": ResistancesFactory.prepare_trap,
        }
        return resistances_dict[name](value)

    @classmethod
    def get_other_info(cls, name: str, value: str):
        other_info_dict = {
            "movement": OtherHeroAttributesFactory.prepare_movement,
            "crit_buff_bonus": OtherHeroAttributesFactory.prepare_crit_buff_bonus,
            "religious": OtherHeroAttributesFactory.prepare_religious,
            "provisions": OtherHeroAttributesFactory.prepare_provisions
        }
        return other_info_dict[name](value)
