import warnings

from base_classes.common import Name
from factories.character_factory import CharacterFactory
from factories.hero_skill_factories import HeroSkillFactory, CampingSkillFactory
from model.skill.camping_skill import CampingSkill
from model.skill.hero_combat_skills.type_vars import DerivedFromBaseSkill
from model.skill.hero_skills import HeroHealSkill, HeroOffensiveSkill
from model.skill.move_skill import MoveSkill

warnings.warn("File to be updated", DeprecationWarning)


class HeroFactory(CharacterFactory):

    @classmethod
    def prepare_combat_move_skill(cls, **kwargs) -> MoveSkill:
        return MoveSkill(HeroSkillFactory) \
            .set_move(kwargs['move']) \
            .set_skill_type(kwargs['type'])

    @classmethod
    def prepare_name(cls, name: str):
        return Name(name)

    @classmethod
    def get_skill(cls, attrs: dict):
        if 'heal' in attrs:
            skill = cls._get_healing_skill(**attrs)
        else:
            skill = cls._get_offensive_skill(**attrs)
        return skill

    @classmethod
    def _set_shared_basic_attrs_to_basic_skill_model(cls, model: DerivedFromBaseSkill,
                                                     limit: str, on_other_heroes: list[str]):
        model \
            .set_limit(limit) \
            .set_on_other_heroes(on_other_heroes)

    @classmethod
    def _get_healing_skill(cls, skill_name: str, launch: list[int], target: list[int], on_target: list[str],
                           on_self: list[str], on_other_heroes: list[str], limit: str, heal: list[str]) \
            -> HeroHealSkill:
        model = HeroHealSkill(HeroSkillFactory)
        cls._set_shared_basic_attrs_to_skill_model(model, skill_name, launch, target, on_target, on_self)
        cls._set_shared_basic_attrs_to_basic_skill_model(model, limit, on_other_heroes)
        return model \
            .set_heal(heal)

    @classmethod
    def _get_offensive_skill(cls, skill_name: str, launch: list[int], target: list[int], on_target: list[str],
                             on_self: list[str], on_other_heroes: list[str], limit: str, on_range: list[str],
                             dmg_mod: list[str], acc: list[str], crit_mod: list[str]) \
            -> HeroOffensiveSkill:
        model = HeroOffensiveSkill(HeroSkillFactory)
        cls._set_shared_basic_attrs_to_skill_model(model, skill_name, launch, target, on_target, on_self)
        cls._set_shared_basic_attrs_to_basic_skill_model(model, limit, on_other_heroes)
        return model \
            .set_on_range(on_range) \
            .set_dmg_mod(dmg_mod) \
            .set_acc(acc) \
            .set_crit_mod(crit_mod)

    @classmethod
    def get_camping_skill(cls, skill_name: str, time_cost: str, target: str, description: str):
        return CampingSkill(CampingSkillFactory) \
            .set_skill_name(skill_name) \
            .set_time_cost(time_cost) \
            .set_target(target) \
            .set_description(description)
