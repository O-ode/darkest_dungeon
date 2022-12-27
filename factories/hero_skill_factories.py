from base_classes.skill_attributes import Heal, CritMod, Accuracy, DmgMod, SkillType, Level, Move, Effect
from constants import SkillBooleans
from factories.base_skill_factories import BaseSkillFactory
from factories.value_modifying_factory import ValueModifyingFactory


class HeroSkillFactory(BaseSkillFactory):
    @classmethod
    def prepare_move(cls, values: list[str]):
        return Move(int(values[0]), int(values[1]))

    @classmethod
    def prepare_effect(cls, value: str):
        return Effect(value)

    @classmethod
    def prepare_skill_booleans(cls, **values):
        return SkillBooleans(ValueModifyingFactory.merge_skill_booleans(**values))

    @classmethod
    def prepare_skill_type(cls, value: str):
        return SkillType(ValueModifyingFactory.str_to_skill_type(value))

    @classmethod
    def prepare_dmg_mod(cls, value: str):
        return DmgMod(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_acc(cls, value: str):
        return Accuracy(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_crit_mod(cls, value: str):
        return CritMod(ValueModifyingFactory.text_to_float_div_100(value))

    @classmethod
    def prepare_heal(cls, values: list[str]):
        return Heal(int(values[0]), int(values[1]))

    @classmethod
    def prepare_level(cls, value: str):
        return Level(ValueModifyingFactory.text_to_int(value))
