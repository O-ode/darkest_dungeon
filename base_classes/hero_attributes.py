from typing import Any, Callable

from base_classes.basic_attribute import BasicAttribute
from base_classes.basic_attribute import Name


class Quirk(BasicAttribute):
    pass


class ResolveLevel(BasicAttribute):
    pass


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
