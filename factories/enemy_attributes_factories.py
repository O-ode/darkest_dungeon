from base_classes.enemy_attributes import HPStygian
from factories.base_attributes_factories import BaseLevelAttributesFactory
from factories.value_modifying_factory import ValueModifyingFactory


class EnemyAttributesFactory(BaseLevelAttributesFactory):

    @classmethod
    def prepare_hp_stygian(cls, value: str) -> HPStygian:
        return HPStygian(ValueModifyingFactory.text_to_int(value))
