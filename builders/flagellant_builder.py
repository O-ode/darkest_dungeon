import warnings

from builders.hero_builder import HeroBuilder
from composites.hero_composite import HeroComposite


class FlagellantBuilder(HeroBuilder):

    def add_quirk_modifiers(self, hero: HeroComposite):
        warnings.warn(f'Method to be updated')
        raise NotImplementedError('')
