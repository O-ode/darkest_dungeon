from abc import abstractmethod

from factories.recistances_factories import ResistancesFactory


class CharacterFactory:

    @classmethod
    @abstractmethod
    def prepare_combat_skill(cls, attrs: dict):
        pass

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
        return resistances_dict[name](value)
