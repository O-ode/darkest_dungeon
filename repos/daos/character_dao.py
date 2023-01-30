from abc import ABC, abstractmethod

from composites.character_composite import CharacterComposite


class CharacterDAO(ABC):

    @classmethod
    @abstractmethod
    def get_combat_skills(cls, character: CharacterComposite):
        pass

    @classmethod
    @abstractmethod
    def get_resistances(cls, character: CharacterComposite):
        pass

    @classmethod
    @abstractmethod
    def get_tags(cls, character: CharacterComposite):
        pass

    @classmethod
    @abstractmethod
    def get_stats(cls, character: CharacterComposite):
        pass
