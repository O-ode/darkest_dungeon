import multiprocessing as mp
from typing import Type, Any

from base_classes.hero_attributes import Quirk, GenerationCondition
from base_classes.hero_stats_composite import HeroStatsComposite
from base_classes.skill_attributes import Effect
from base_classes.type_vars import ResistanceType
from factories.hero_factory import HeroFactory
from model.character_model import CharacterComposite
from model.skill.camping_skill import CampingSkill
from model.skill.hero_combat_skills.type_vars import HeroCombatSkillTypes
from model.skill.move_skill import MoveSkill

logger = mp.get_logger()


class HeroComposite(CharacterComposite):

    def __init__(self, factory: Type[HeroFactory]):
        super(HeroComposite, self).__init__(factory)
        self._combat_move_skill: MoveSkill or None = None

        self._camping_skills: list[CampingSkill] = []
        self._combat_skills: list[HeroCombatSkillTypes] = []
        self._deaths_door_effects: list[Effect] = []
        self._generation_conditions: list[GenerationCondition] = []
        self._crit_effects: list[Effect] = []
        self._quirk_modifiers: list[Quirk] = []
        self._resistances: list[ResistanceType] = []

    def get_stats(self) -> list[HeroStatsComposite]:
        return self._stats

    def get_combat_skills(self) -> list[HeroCombatSkillTypes]:
        return self._combat_skills

    def get_generation_conditions(self):
        return self._generation_conditions

    # def get_weapons(self) -> list[Weapon]:
    #     return self._weapons

    def get_resistances(self) -> list[ResistanceType]:
        return self._resistances

    def get_quirk_modifiers(self) -> list[Quirk]:
        return self._quirk_modifiers

    def get_crit_effects(self) -> list[Effect]:
        return self._crit_effects

    def get_deaths_door_effects(self) -> list[Effect]:
        return self._deaths_door_effects

    def get_camping_skills(self) -> list[CampingSkill]:
        return self._camping_skills

    # def get_armors(self) -> list[Armor]:
    #     return self._armors

    def get_combat_move_skill(self) -> MoveSkill:
        return self._combat_move_skill

    def add_camping_skill(self, skill: CampingSkill):
        self._camping_skills.append(skill)
        return self

    # def add_combat_skill(self, skill: HeroCombatSkillTypes):
    #     super(HeroModel, self).add_combat_skill(skill)
    #     # self._combat_skills.append(skill)
    #     return self

    def add_quirk_modifier(self, value: Any):
        raise NotImplementedError('lel')
        # self._quirk_modifiers.append(HeroFactory)
        # return self

    def add_deaths_door_effect(self, value: str):
        self._deaths_door_effects.append(HeroFactory.prepare_deaths_door_effect(value))
        return self

    def add_crit_effect(self, value: str):
        self._crit_effects.append(HeroFactory.prepare_crit_effect(value))
        return self

    def add_resistance(self, name: str, value: str):
        self._resistances.append(HeroFactory.prepare_resistance(name, value))
        return self

    # def add_armor(self, armor: Armor):
    #     self._armors.append(armor)
    #     return self
    #
    # def add_weapon(self, weapon: Weapon):
    #     self._weapons.append(weapon)
    #     return self

    def add_generation_condition(self, name: str, value: str):
        self._generation_conditions.append(HeroFactory.prepare_generation_condition(name, value))
        return self

    def set_combat_move_skill(self, **kwargs):
        self._combat_move_skill = self._factory.prepare_combat_move_skill(**kwargs)
        return self

    def __repr__(self):
        return str(vars(self))
