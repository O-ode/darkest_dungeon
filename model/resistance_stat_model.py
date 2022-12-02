from constants import pretty


class ResistanceStatModel:
    def __init__(self, bleed=None, blight=None, debuff=None, death_blow=None,
                 disease=None, move=None, stun=None, trap=None):
        self.bleed: float = bleed
        self.blight: float = blight
        self.debuff: float = debuff
        self.death_blow: float = death_blow
        self.disease: float = disease
        self.move: float = move
        self.stun: float = stun
        self.trap: float = trap

    def __repr__(self):
        return pretty(self.__dict__)

    def __str__(self):
        return pretty(self.__dict__)
