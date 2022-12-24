import logging
import warnings
from typing import Any, Generator

from model.enemy_model import EnemyModel

warnings.warn("File to be updated", DeprecationWarning)
logger = logging.getLogger()


class EnemyDAO:
    @classmethod
    def get_level_attributes(cls, enemy: EnemyModel) -> Generator[dict[str, str], Any, None]:
        pass
        # raw_attributes = \
        #     [[WebElementValueFactory.str_underscored_lower_from_inner_text(element) for element in elements_row]
        #      for elements_row in EnemySeleniumDAO.get_level_attributes_elements(enemy)]

        # raw_attributes = {row[0]: row[1] for row in raw_attributes}
        # raw_attributes['hp_stygian'] = raw_attributes.pop('hp_(stygian/bloodmoon)')
        # for i in range(5):
        #     level_attrs = {name: values[i] for name, values in raw_attributes.items()}
        #     logger.info(pretty(level_attrs))
        #     yield level_attrs

    @classmethod
    def get_resistances(cls, enemy) -> Generator[dict[str, str], Any, None]:
        pass

    # for name_element, value_element in EnemySeleniumDAO.get_resistances(enemy):
    #     resistance_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
    #     resistance_value = WebElementValueFactory.str_text_from_inner_text(value_element)
    #     yield {'name': resistance_name, 'value': resistance_value}

    @classmethod
    def get_other_info(cls, enemy) -> Generator[dict[str, str], Any, None]:
        pass

    # for name_element, value_element in EnemySeleniumDAO.get_other_info(enemy):
    #     other_attribute_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
    #     other_attribute_value = WebElementValueFactory.str_text_from_inner_text(value_element)
    #     yield {'name': other_attribute_name, 'value': other_attribute_value}

    @classmethod
    def get_skills(cls, enemy) -> Generator[dict[str, str], Any, None]:
        pass

# for i, skill_table_attrs in enumerate(EnemySeleniumDAO.get_skills(enemy)):
#     factory_values = {}
#
#     skill_name = WebElementValueFactory.str_underscored_lower_from_inner_text(skill_table_attrs["skill_name"])
#     factory_values['skill_name'] = skill_name
#
#     if 'limit' in skill_table_attrs.keys():
#         limit = WebElementValueFactory.str_text_from_inner_text(skill_table_attrs["limit"])
#     else:
#         limit = None
#     factory_values['limit'] = limit
#
#     skill_attribute_names = \
#         [WebElementValueFactory.str_underscored_lower_from_inner_text(e)
#          for e in skill_table_attrs['title_elements']]
#
#     temp_values = {zipped[0]: [v for v in zipped[1:] if v is not None]
#                    for zipped in itertools.zip_longest(
#             *[skill_attribute_names, *skill_table_attrs['value_elements']]
#         )}
#
#     for attr_name, attr_values in temp_values.items():
#         if 'effect' == attr_name:
#             _, value_factory_method = skill_kwargs[attr_name]
#             on_target_on_other_heroes = {'on_target': [], 'on_other_heroes': []}
#             for value in attr_values:
#                 res = value_factory_method(value)
#                 on_target_on_other_heroes['on_target'].append(res['on_target'])
#                 on_target_on_other_heroes['on_other_heroes'].append(res['on_other_heroes'])
#             factory_values.update(on_target_on_other_heroes)
#         else:
#             skill_attr_name, value_factory_method = skill_kwargs[attr_name]
#             transformed_values = [value_factory_method(value) for value in attr_values]
#
#             factory_values[skill_attr_name] = transformed_values[0] \
#                 if len(transformed_values) == 1 \
#                    and attr_name not in ['damage', 'accuracy', 'crit_mod', 'effect', 'self', 'heal'] \
#                 else transformed_values
#
#     logger.info(f'factory_values: {pretty(factory_values)}')
#     yield factory_values
