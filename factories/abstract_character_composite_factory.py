import re
from abc import ABC, abstractmethod

from base_classes.character_attributes import Tag
from base_classes.basic_attribute import Name
from factories.recistances_factories import ResistancesFactory


class AbstractCharacterCompositeFactory(ABC):

    @classmethod
    def prepare_name(cls, name: str):
        return Name(re.search(r'[\s\w]+', name).group())

    @classmethod
    def prepare_resistance(cls, name: str, value: str):
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
        # f = resistances_dict[name]
        # a = f(value)
        return resistances_dict[name](value)

    @classmethod
    def prepare_tag(cls, value: str):
        return Tag(value)

    @classmethod
    @abstractmethod
    def prepare_stats(cls, **stats_attrs):
        pass

    @classmethod
    @abstractmethod
    def prepare_combat_skill(cls, **skill_attrs):
        pass
