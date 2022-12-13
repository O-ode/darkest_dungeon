from abc import abstractmethod
from typing import Type

from base_classes.type_vars import DerivedFromBasicAttributes
from factories.hero_attributes_factories import ResistancesFactory
from model.skill.type_vars import DerivedFromBaseSkill


class CharacterFactory:

    @classmethod
    @abstractmethod
    def get_skill(cls, attrs: dict):
        pass

    @classmethod
    def _set_shared_attrs_to_character_model(cls, model: DerivedFromBasicAttributes, level: str,
                                             hp: str, dodge: str, prot: str, spd: str):
        return model.set_level(level) \
            .set_hp(hp) \
            .set_dodge(dodge) \
            .set_prot(prot) \
            .set_spd(spd)

    @classmethod
    def _set_shared_basic_attrs_to_skill_model(cls, model: DerivedFromBaseSkill, skill_name: str,
                                               rank: list[int], target: list[int], on_target: [str], on_self: [str]):
        return model.set_skill_name(skill_name) \
            .set_rank(rank) \
            .set_target(target) \
            .set_on_target(on_target) \
            .set_on_self(on_self)

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
