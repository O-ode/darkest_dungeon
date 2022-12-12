from factories.web_element_value_factory import WebElementValueFactory

skill_kwargs = {
    "range": ("on_range", WebElementValueFactory.str_text_from_inner_text),
    "rank": ("rank", WebElementValueFactory.value_from_dots),
    "target": ("target", WebElementValueFactory.value_from_dots),
    "damage": ("dmg_mod", WebElementValueFactory.str_text_from_inner_text),
    "accuracy": ("acc", WebElementValueFactory.str_text_from_inner_text),
    "crit_mod": ("crit_mod", WebElementValueFactory.str_text_from_inner_text),
    "effect": ("effect", WebElementValueFactory.subdivide_hero_effects_from_inner_text),
    "self": ("on_self", WebElementValueFactory.str_text_from_inner_text),
    "heal": ("heal", WebElementValueFactory.str_text_from_inner_text)
}

# skill_kwargs = {
#     "Range": ("on_range", str_from_inner_text, do_nothing),
#     "Rank": ("rank", value_from_dots, do_nothing),
#     "Target": ("target", value_from_dots, do_nothing),
#     "Damage": ("dmg_mod", str_from_inner_text, text_to_float_div_100),
#     "Accuracy": ("acc", str_from_inner_text, text_to_int),
#     "Crit mod": ("crit_mod", str_from_inner_text, text_to_float_div_100),
#     "Effect": ("effects", str_from_inner_text, text_to_effects_dict),
#     "Self": ("on_self", str_from_inner_text, text_to_effect_per_line),
#     "Heal": ("heal", str_from_inner_text, do_nothing)
# }
