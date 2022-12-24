import logging
import warnings

from model.hero_model import HeroModel
from repos.daos.text_reader_daos.constants import HERO_FILES
from repos.file_repo import FileRepo

warnings.warn("File to be updated, lacking methods", DeprecationWarning)
logger = logging.getLogger()


class HeroDAO:
    @classmethod
    def get_resistances_for_hero(cls, hero: HeroModel):
        class_name = hero.get_name()
        relative_path, file_name = HERO_FILES[class_name]
        resistances = FileRepo.get_dict_from_file(relative_path, file_name)['resistances']
        for k, v in iter(resistances.items()):
            yield {"name": k, "value": v}

    #     @classmethod
#     def get_level_attributes(cls, hero: HeroModel) -> Generator[dict[str, str], Any, None]:
#         raw_attributes = \
#             [[WebElementValueFactory.str_underscored_lower_from_inner_text(element) for element in elements_row]
#              for elements_row in HeroSeleniumDAO.get_level_attributes_elements(hero)]
#
#         raw_attributes = {row[0]: row[1:] for row in raw_attributes}
#         for i in range(5):
#             level_attrs = {name: values[i] for name, values in raw_attributes.items()}
#             logger.info(pretty(level_attrs))
#             yield level_attrs
#
#     @classmethod
#     def get_resistances(cls, hero) -> Generator[dict[str, str], Any, None]:
#         for name_element, value_element in HeroSeleniumDAO.get_resistances(hero):
#             resistance_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
#             resistance_value = WebElementValueFactory.str_text_from_inner_text(value_element)
#             yield {'name': resistance_name, 'value': resistance_value}
#
#     @classmethod
#     def get_other_info(cls, hero) -> Generator[dict[str, str], Any, None]:
#         for name_element, value_element in HeroSeleniumDAO.get_other_info(hero):
#             other_attribute_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
#             other_attribute_value = WebElementValueFactory.str_text_from_inner_text(value_element)
#             yield {'name': other_attribute_name, 'value': other_attribute_value}
#
#     @classmethod
#     def get_camping_skills(cls, hero):
#         attr_names = ['skill_name', 'time_cost', 'target', 'description']
#         for value_elements in HeroSeleniumDAO.get_camping_skills(hero):
#             yield {attr_name: WebElementValueFactory.str_text_from_inner_text(value_element)
#                    for attr_name, value_element in zip(attr_names, value_elements)}
#
#     @classmethod
#     def get_skills(cls, hero) -> Generator[dict[str, str], Any, None]:
#
#         for i, skill_table_attrs in enumerate(HeroSeleniumDAO.get_skills(hero)):
#             factory_values = {}
#
#             skill_name = WebElementValueFactory.str_underscored_lower_from_inner_text(skill_table_attrs["skill_name"])
#             factory_values['skill_name'] = skill_name
#
#             if 'limit' in skill_table_attrs.keys():
#                 limit = WebElementValueFactory.str_text_from_inner_text(skill_table_attrs["limit"])
#             else:
#                 limit = None
#             factory_values['limit'] = limit
#
#             skill_attribute_names = \
#                 [WebElementValueFactory.str_underscored_lower_from_inner_text(e)
#                  for e in skill_table_attrs['title_elements']]
#
#             temp_values = {zipped[0]: [v for v in zipped[1:] if v is not None]
#                            for zipped in itertools.zip_longest(
#                     *[skill_attribute_names, *skill_table_attrs['value_elements']]
#                 )}
#
#             for attr_name, attr_values in temp_values.items():
#                 if 'effect' == attr_name:
#                     _, value_factory_method = skill_kwargs[attr_name]
#                     on_target_on_other_heroes = {'on_target': [], 'on_other_heroes': []}
#                     for value in attr_values:
#                         res = value_factory_method(value)
#                         on_target_on_other_heroes['on_target'].append(res['on_target'])
#                         on_target_on_other_heroes['on_other_heroes'].append(res['on_other_heroes'])
#                     factory_values.update(on_target_on_other_heroes)
#                 else:
#                     skill_attr_name, value_factory_method = skill_kwargs[attr_name]
#                     transformed_values = [value_factory_method(value) for value in attr_values]
#
#                     factory_values[skill_attr_name] = transformed_values[0] \
#                         if len(transformed_values) == 1 \
#                            and attr_name not in ['damage', 'accuracy', 'crit_mod', 'effect', 'self', 'heal'] \
#                         else transformed_values
#
#             logger.info(f'factory_values: {pretty(factory_values)}')
#             yield factory_values
