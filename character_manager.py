from factories.hero_level_attributes import HeroResolveAttributesModel, HeroResolveAttributesFactory


def get_hero_attributes_from_transformed_attrs(transformed_attrs: dict) -> list[HeroResolveAttributesModel]:
    return [HeroResolveAttributesModel(HeroResolveAttributesFactory())
            .set_values(resolve_level=resolve_level, **attributes_dict)
            for resolve_level, attributes_dict in transformed_attrs.items()]
