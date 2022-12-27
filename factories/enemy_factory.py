from factories.character_factory import CharacterFactory


class EnemyFactory(CharacterFactory):
    @classmethod
    def prepare_combat_skill(cls, attrs: dict):
        pass

    @classmethod
    def get_skill(cls, attrs: dict):
        raise NotImplementedError()
