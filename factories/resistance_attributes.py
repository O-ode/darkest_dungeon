from factories.attribute_base import AttributeBase
from selenium_local.text_modifying_functions import text_to_float_div_100


class Stun(AttributeBase):
    pass


class Move(AttributeBase):
    pass


class Blight(AttributeBase):
    pass


class Bleed(AttributeBase):
    pass


class Disease(AttributeBase):
    pass


class Debuff(AttributeBase):
    pass


class DeathBlow(AttributeBase):
    pass


class Trap(AttributeBase):
    pass


class HeroResistancesFactory:

    @classmethod
    def set_stun(cls, value: str) -> Stun:
        return Stun(text_to_float_div_100(value))

    @classmethod
    def set_move(cls, value: str) -> Move:
        return Move(text_to_float_div_100(value))

    @classmethod
    def set_blight(cls, value: str) -> Blight:
        return Blight(text_to_float_div_100(value))

    @classmethod
    def set_bleed(cls, value: str) -> Bleed:
        return Bleed(text_to_float_div_100(value))

    @classmethod
    def set_disease(cls, value: str) -> Disease:
        return Disease(text_to_float_div_100(value))

    @classmethod
    def set_debuff(cls, value: str) -> Debuff:
        return Debuff(text_to_float_div_100(value))

    @classmethod
    def set_death_blow(cls, value: str) -> DeathBlow:
        return DeathBlow(text_to_float_div_100(value))

    @classmethod
    def set_trap(cls, value: str) -> Trap:
        return Trap(text_to_float_div_100(value))


class HeroResistances:

    def __init__(self, factory: HeroResistancesFactory):
        self.factory = factory
        self.stun: Stun or None = None
        self.move: Move or None = None
        self.blight: Blight or None = None
        self.bleed: Bleed or None = None
        self.disease: Disease or None = None
        self.debuff: Debuff or None = None
        self.death_blow: DeathBlow or None = None
        self.trap: Trap or None = None

    def set_values(self, stun=None, move=None, blight=None, bleed=None,
                   disease=None, debuff=None, death_blow=None, trap=None):
        self.stun = self.factory.set_stun(stun)
        self.move = self.factory.set_move(move)
        self.blight = self.factory.set_blight(blight)
        self.bleed = self.factory.set_bleed(bleed)
        self.disease = self.factory.set_disease(disease)
        self.debuff = self.factory.set_debuff(debuff)
        self.death_blow = self.factory.set_death_blow(death_blow)
        self.trap = self.factory.set_trap(trap)
        return self
