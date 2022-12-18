from factories.character_factory import CharacterFactory
from factories.hero_attributes_factories import HeroLevelAttributesFactory, OtherHeroAttributesFactory
from factories.hero_skill_factories import HeroSkillFactory, CampingSkillFactory
from model.character_attributes.hero_attributes import HeroLevelAttributesModel
from model.skill.camping_skill import CampingSkill
from model.skill.hero_skills import HeroSupportSkill, HeroHealSkill, HeroOffensiveSkill
from model.skill.type_vars import DerivedFromHeroBaseSkill


class HeroFactory(CharacterFactory):

    @classmethod
    def get_skill(cls, attrs: dict):
        if 'dmg_mod' in attrs:
            skill = cls._get_offensive_skill(**attrs)
        elif 'heal' in attrs.keys():
            skill = cls._get_healing_skill(**attrs)
        else:
            skill = cls._get_support_skill(**attrs)
        return skill

    @classmethod
    def _set_shared_basic_attrs_to_basic_skill_model(cls, model: DerivedFromHeroBaseSkill,
                                                     limit: str, on_other_heroes: list[str]):
        model \
            .set_limit(limit) \
            .set_on_other_heroes(on_other_heroes)

    @classmethod
    def _get_support_skill(cls, skill_name: str, rank: list[int], target: list[int],
                           on_target: list[str], on_self: list[str], on_other_heroes: list[str], limit: str) \
            -> HeroSupportSkill:
        model = HeroSupportSkill(HeroSkillFactory)

        cls._set_shared_basic_attrs_to_skill_model(model, skill_name, rank, target, on_target, on_self)
        cls._set_shared_basic_attrs_to_basic_skill_model(model, limit, on_other_heroes)
        return model

    @classmethod
    def _get_healing_skill(cls, skill_name: str, rank: list[int], target: list[int], on_target: list[str],
                           on_self: list[str], on_other_heroes: list[str], limit: str, heal: list[str]) \
            -> HeroHealSkill:
        model = HeroHealSkill(HeroSkillFactory)
        cls._set_shared_basic_attrs_to_skill_model(model, skill_name, rank, target, on_target, on_self)
        cls._set_shared_basic_attrs_to_basic_skill_model(model, limit, on_other_heroes)
        return model \
            .set_heal(heal)

    @classmethod
    def _get_offensive_skill(cls, skill_name: str, rank: list[int], target: list[int], on_target: list[str],
                             on_self: list[str], on_other_heroes: list[str], limit: str, on_range: list[str],
                             dmg_mod: list[str], acc: list[str], crit_mod: list[str]) \
            -> HeroOffensiveSkill:
        model = HeroOffensiveSkill(HeroSkillFactory)
        cls._set_shared_basic_attrs_to_skill_model(model, skill_name, rank, target, on_target, on_self)
        cls._set_shared_basic_attrs_to_basic_skill_model(model, limit, on_other_heroes)
        return model \
            .set_on_range(on_range) \
            .set_dmg_mod(dmg_mod) \
            .set_acc(acc) \
            .set_crit_mod(crit_mod)

    @classmethod
    def get_level_attributes_model(cls, resolve: str, max_hp: str, dodge: str, prot: str,
                                   spd: str, acc_mod: str, crit: str, dmg: str) \
            -> HeroLevelAttributesModel:
        model = HeroLevelAttributesModel(HeroLevelAttributesFactory)
        cls._set_shared_attrs_to_character_model(model, resolve, max_hp, dodge, prot, spd)

        return model \
            .set_acc_mod(acc_mod) \
            .set_crit(crit) \
            .set_dmg(dmg)

    @classmethod
    def get_other_info(cls, name: str, value: str):
        other_info_dict = {
            "movement": OtherHeroAttributesFactory.prepare_movement,
            "crit_buff_bonus": OtherHeroAttributesFactory.prepare_crit_buff_bonus,
            "religious": OtherHeroAttributesFactory.prepare_religious,
            "provisions": OtherHeroAttributesFactory.prepare_provisions
        }

        return other_info_dict[name](value)

    @classmethod
    def get_camping_skill(cls, skill_name: str, time_cost: str, target: str, description: str):
        return CampingSkill(CampingSkillFactory) \
            .set_skill_name(skill_name) \
            .set_time_cost(time_cost) \
            .set_target(target) \
            .set_description(description)
