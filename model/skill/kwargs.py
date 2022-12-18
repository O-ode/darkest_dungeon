from factories.web_element_value_factory import WebElementValueFactory

skill_kwargs = {
    "range": ("on_range", WebElementValueFactory.str_text_from_inner_text),
    "rank": ("rank", WebElementValueFactory.inverted_value_from_dots),
    "target": ("target", WebElementValueFactory.value_from_dots),
    "damage": ("dmg_mod", WebElementValueFactory.str_text_from_inner_text),
    "accuracy": ("acc", WebElementValueFactory.str_text_from_inner_text),
    "crit_mod": ("crit_mod", WebElementValueFactory.str_text_from_inner_text),
    "effect": ("effect", WebElementValueFactory.subdivide_hero_effects_from_inner_text),
    "self": ("on_self", WebElementValueFactory.str_text_from_inner_text),
    "heal": ("heal", WebElementValueFactory.str_text_from_inner_text)
}
