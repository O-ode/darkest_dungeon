from abc import ABC, abstractmethod

from base_classes.stats_attributes import HP, Spd, Prot, Dodge
from constants import pretty


class StatsBaseComposite(ABC):

    @abstractmethod
    def set_hp(self, value: str):
        pass

    @abstractmethod
    def set_spd(self, value: str):
        pass

    @abstractmethod
    def set_prot(self, value: str):
        pass

    @abstractmethod
    def set_dodge(self, value: str):
        pass

    @abstractmethod
    def get_hp(self) -> HP:
        pass

    @abstractmethod
    def get_spd(self) -> Spd:
        pass

    @abstractmethod
    def get_prot(self) -> Prot:
        pass

    @abstractmethod
    def get_dodge(self) -> Dodge:
        pass

    def __repr__(self):
        return pretty(vars(self))
