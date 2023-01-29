from typing import Any, Callable

from base_classes.basic_attribute import BasicAttribute
from base_classes.basic_attribute import Name
from base_classes.skill_attributes import Effect


class Quirk(BasicAttribute):
    pass


class ResolveLevel(BasicAttribute):
    pass


class DeathsDoor:
    def __init__(self, buffs: list[Effect], recovery_buffs: list[Effect], recovery_heart_attack_buffs: list[Effect],
                 enter_effects: list[Effect], enter_effect_round_cooldown: int):
        self.buffs = buffs
        self.recovery_buffs = recovery_buffs
        self.recovery_heart_attack_buffs = recovery_heart_attack_buffs
        self.enter_effects = enter_effects
        self.enter_effect_round_cooldown = enter_effect_round_cooldown


class GenerationCondition:

    def __init__(self, factory_method: Callable[[str], Any]):
        self._factory_method: Callable[[str], Any] = factory_method
        self._name: Name or None = None
        self._value: Any = None

    def set_name(self, value: str):
        self._name = Name(value)
        return self

    def set_value(self, value: str):
        self._value = self._factory_method(value)
        return self

    def get_name(self) -> Name:
        return self._name

    def get_value(self):
        return self._value
