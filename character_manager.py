from factories.hero_level_attributes import HeroResolveLevelAttributes, HeroResolveLevelAttributesFactory


def get_hero_attributes_from_transformed_attrs(transformed_attrs: dict) -> list[HeroResolveLevelAttributes]:
    return [HeroResolveLevelAttributes(HeroResolveLevelAttributesFactory())
            .get_values(resolve_level=resolve_level, **attributes_dict)
            for resolve_level, attributes_dict in transformed_attrs.items()]
