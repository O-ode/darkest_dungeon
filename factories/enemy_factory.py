from factories.character_factory import CharacterFactory
from factories.enemy_attributes_factories import EnemyAttributesFactory
from model.character_attributes.enemy_attributes_model import EnemyAttributesModel
from model.skill.type_vars import DerivedFromBaseSkill


class EnemyFactory(CharacterFactory):

    @classmethod
    def _set_shared_basic_attrs_to_basic_skill_model(cls, model: DerivedFromBaseSkill,
                                                     limit: str, on_other_heroes: list[str]):
        model \
            .set_limit(limit) \
            .set_on_other_heroes(on_other_heroes)

    @classmethod
    def get_level_attributes_model(cls, hp: str, hp_stygian: str, dodge: str, prot: str,
                                   spd: str, stealth: str) \
            -> EnemyAttributesModel:
        model = EnemyAttributesModel(EnemyAttributesFactory)
        cls._set_shared_attrs_to_character_model(model, resolve, max_hp, dodge, prot, spd)

        return model \
            .set_acc_mod(acc_mod) \
            .set_crit(crit) \
            .set_dmg(dmg)
