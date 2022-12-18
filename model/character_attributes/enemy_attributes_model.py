from typing import Any, Type

from base_classes.enemy_attributes import HPStygian
from factories.enemy_attributes_factories import EnemyAttributesFactory
from model.character_attributes.base_attributes import BaseLevelAttributesModel


class EnemyAttributesModel(BaseLevelAttributesModel):

    def __init__(self, factory: Type[EnemyAttributesFactory]):
        super(EnemyAttributesModel, self).__init__(factory)
        self._hp_stygian: HPStygian or None = None

    def set_hp_stygian(self, value: Any):
        self._hp_stygian = self._factory.prepare_hp_stygian(value)
        return self

    def get_hp_stygian(self):
        return self._hp_stygian
