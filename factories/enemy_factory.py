from factories.abstract_character_composite_factory import AbstractCharacterCompositeFactory


class EnemyFactory(AbstractCharacterCompositeFactory):
    @classmethod
    def prepare_stats(cls, **stats_attrs):
        pass

    @classmethod
    def prepare_hp(cls, value: str):
        pass

    @classmethod
    def prepare_spd(cls, value: str):
        pass

    @classmethod
    def prepare_prot(cls, value: str):
        pass

    @classmethod
    def prepare_dodge(cls, value: str):
        pass

    @classmethod
    def prepare_combat_skill(cls, attrs: dict):
        pass
