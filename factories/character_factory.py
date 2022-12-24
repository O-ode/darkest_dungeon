import warnings
from abc import abstractmethod

from factories.recistances_factories import ResistancesFactory
from model.skill.hero_combat_skills.type_vars import DerivedFromBaseSkill


class CharacterFactory:

    @classmethod
    @abstractmethod
    def get_skill(cls, attrs: dict):
        pass

    @classmethod
    def _set_shared_basic_attrs_to_skill_model(cls, model: DerivedFromBaseSkill, skill_name: str,
                                               launch: list[int], target: list[int], on_target: [str], on_self: [str]):
        warnings.warn("Method is currently not usable", DeprecationWarning)
        return model.set_skill_name(skill_name) \
            .set_launch(launch) \
            .set_target(target) \
            .set_on_target(on_target) \
            .set_on_self(on_self)

    @classmethod
    def get_resistance_factory_method(cls, name: str, value: str):
        resistances_dict = {
            "stun": ResistancesFactory.prepare_stun,
            "move": ResistancesFactory.prepare_move,
            "poison": ResistancesFactory.prepare_blight,
            "bleed": ResistancesFactory.prepare_bleed,
            "disease": ResistancesFactory.prepare_disease,
            "debuff": ResistancesFactory.prepare_debuff,
            "death_blow": ResistancesFactory.prepare_death_blow,
            "trap": ResistancesFactory.prepare_trap,
        }
        return resistances_dict[name](value)
