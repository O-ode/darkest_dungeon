from factories.character_factory import CharacterFactory


class EnemyFactory(CharacterFactory):
    @classmethod
    def get_skill(cls, attrs: dict):
        raise NotImplementedError()
