from constants import Range, pretty
from model.effect_model import EffectModel


class SkillModel:
    def __init__(self, skill_name=None, on_range=None, rank=None, target=None,
                 dmg_mod=None, acc=None, crit_mod=None, effects=None, on_self=None,
                 heal=None):
        self.skill_name: str = skill_name
        self.on_range: Range = on_range
        self.rank: [int] = rank
        self.target: [int] or str = target
        self.dmg_mod: float = dmg_mod
        self.acc: int = acc
        self.crit_mod: float = crit_mod
        self.effects: {str: list[EffectModel]} = effects
        self.on_self: [EffectModel] = on_self
        self.heal: str = heal

    def __repr__(self):
        return pretty(self.__dict__)

    def __str__(self):
        return pretty(self.__dict__)

    def __hash__(self):
        return hash(self.skill_name)
