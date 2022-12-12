from base_classes.character_attributes import Crit
from base_classes.skill_attributes import Note, Accuracy, Dmg, Range
from factories.base_skill_factories import BaseSkillFactory
from factories.value_modifying_factory import ValueModifyingFactory


class EnemySkillFactory(BaseSkillFactory):

    @classmethod
    def prepare_range(cls, value: str):
        return Range(ValueModifyingFactory.str_to_range_enum(value))

    @classmethod
    def prepare_dmg(cls, value: str):
        return Dmg(*ValueModifyingFactory.text_to_hp_modification_value(value))

    @classmethod
    def prepare_acc(cls, value: str):
        return Accuracy(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_crit_chance(cls, value: str) -> Crit:
        return Crit(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_notes(cls, value: str) -> [Note]:
        return [Note(v) for v in value]
