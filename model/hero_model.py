import multiprocessing as mp
from typing import Any, Type

from base_classes.character_attributes import Tag
from base_classes.common import Name
from base_classes.hero_attributes import Quirk
from base_classes.skill_attributes import Effect
from base_classes.type_vars import ResistanceType
from factories.hero_factory import HeroFactory
from model.armor_model import Armor
from model.skill.camping_skill import CampingSkill
from model.skill.hero_combat_skills.type_vars import HeroCombatSkillTypes
from model.skill.move_skill import MoveSkill
from model.weapon_model import Weapon

logger = mp.get_logger()


class HeroModel:

    def __init__(self, factory: Type[HeroFactory]):
        self._factory: Type[HeroFactory] = factory
        self._name: Name or None = None
        self._combat_move_skill: MoveSkill or None = None

        self._armors: list[Armor] = []
        self._camping_skills: list[CampingSkill] = []
        self._combat_skills: list[HeroCombatSkillTypes] = []
        self._deaths_door_effects: list[Effect] = []
        self._crit_effects: list[Effect] = []
        self._quirk_modifiers: list[Quirk] = []
        self._resistances: list[ResistanceType] = []
        self._tags: list[Tag] = []
        self._weapons: list[Weapon] = []

    def get_weapons(self) -> list[Weapon]:
        return self._weapons

    def get_tags(self) -> list[Tag]:
        return self._tags

    def get_resistances(self) -> list[ResistanceType]:
        return self._resistances

    def get_quirk_modifiers(self) -> list[Quirk]:
        return self._quirk_modifiers

    def get_crit_effects(self) -> list[Effect]:
        return self._crit_effects

    def get_deaths_door_effects(self) -> list[Effect]:
        return self._deaths_door_effects

    def get_combat_skills(self) -> list[HeroCombatSkillTypes]:
        return self._combat_skills

    def get_camping_skills(self) -> list[CampingSkill]:
        return self._camping_skills

    def get_armors(self) -> list[Armor]:
        return self._armors

    def get_name(self) -> Name:
        return self._name

    def get_combat_move_skill(self) -> MoveSkill:
        return self._combat_move_skill

    def add_camping_skill(self, skill: CampingSkill):
        self._camping_skills.append(skill)
        return self

    def add_combat_skill(self, skill: HeroCombatSkillTypes):
        self._combat_skills.append(skill)
        return self

    def add_quirk_modifier(self, quirk: Quirk):
        self._quirk_modifiers.append(quirk)
        return self

    def add_deaths_door_effect(self, effect: Effect):
        self._deaths_door_effects.append(effect)
        return self

    def add_crit_effect(self, crit_effect: Effect):
        self._crit_effects.append(crit_effect)
        return self

    def add_tag(self, tag: Tag):
        self._tags.append(tag)
        return self

    def add_resistance(self, resistance: ResistanceType):
        self._resistances.append(resistance)
        return self

    def add_armor(self, armor: Armor):
        self._armors.append(armor)
        return self

    def add_weapon(self, weapon: Weapon):
        self._weapons.append(weapon)
        return self

    def set_name(self, value: Any):
        self._name = self._factory.prepare_name(value)
        return self

    def set_combat_move_skill(self, **kwargs):
        self._combat_move_skill = self._factory.prepare_combat_move_skill(**kwargs)
        return self

    def __repr__(self):
        return str(vars(self))
