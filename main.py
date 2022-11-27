import datetime
import logging
import os.path
import re
import sqlite3
import traceback
from pprint import pformat

import unicodedata
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from constants import skill_attributes_regex, skill_kwargs, character_level_kwargs
from model.character_level_model import CharacterLevelModel
from model.character_model import CharacterModel
from model.skill_model import SkillModel


# def get_classes():
#     driver.get("https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)")
#     try:
#         wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
#     except:
#         pass
#
#     wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))
#
#     table = driver.find_element(By.CSS_SELECTOR, '#toc > ul > li.toclevel-1.tocsection-17')
#     class_names = [re.search(r"[a-zA-Z\- ]+$", e.get_attribute("innerText")).group().lstrip() for e in
#                    table.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]')]
#     pprint(class_names, indent=2, depth=4)
#     return class_names


def get_characters():
    driver.get("https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)")
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
    except:
        pass

    wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))

    section_names = [f'li[class="toclevel-1 tocsection-17"]',
                     f'li[class="toclevel-1 tocsection-34"]']
    _characters = []
    for s_name in section_names:
        section = driver.find_element(By.CSS_SELECTOR, s_name)
        for el in section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]'):
            name = re.search(r"[a-zA-Z\s-]*$", el.get_attribute("innerText")).group().lstrip()
            _characters.append(CharacterModel(name))

    logger.info(f'Character list: {pformat([_character.name for _character in _characters])}')
    yield from _characters


def get_skills():
    logger.debug(f'Getting skills')
    wait.until(EC.presence_of_element_located(
        (By.XPATH, f'//span[text()="Combat Skills" or text()="Combat Abilities"]')))

    for table in driver.find_elements(By.CSS_SELECTOR, f'table.wikitable.tablebg'):
        try:
            skill_name = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > th').get_attribute('innerText')
            skip_regex = re.compile(r'(Expand|Further\s*levels)', re.I)
            if skip_regex.search(skill_name):
                continue
            logger.debug(f'skill_name: {skill_name}')
            kwargs = {"skill_name": skill_name}
        except Exception as e:
            # yield SkillModel(f'Error{i}', [f'{type(e)}:\n{traceback.format_exc()}'])
            logger.error(traceback.format_exc())
            continue
        try:
            info_row = table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(3)")
        except Exception as e:
            # yield SkillModel(f'Error{i}', [f'{type(e)}:\n{traceback.format_exc()}'])
            logger.error(traceback.format_exc())
            continue
        try:
            titles_row = table.find_element(By.CSS_SELECTOR, 'tbody > tr[class="accent1tablecell"]')
        except Exception as e:
            # yield SkillModel(f'Error{i}', [f'{type(e)}:\n{traceback.format_exc()}'])
            logger.error(traceback.format_exc())
            continue

        for _i, col in enumerate(titles_row.find_elements(By.CSS_SELECTOR, 'td')[1:], start=1):
            skill_attribute_name = unicodedata.normalize('NFKD', col.get_attribute('innerText'))
            logger.debug(skill_attribute_name)
            skill_attribute_name = skill_attributes_regex.search(skill_attribute_name).group()
            skill_attribute_name, value_obtaining_function, value_modifying_function = \
                skill_kwargs[skill_attribute_name]

            value = info_row.find_element(By.CSS_SELECTOR, f'td:nth-child({_i})')
            value = value_obtaining_function(value)
            value = value_modifying_function(value)

            kwargs[skill_attribute_name] = value

        logger.debug(f'kwargs:\n{pformat(kwargs)}')
        skill = SkillModel(**kwargs)
        logger.info(f'New skill: {skill}')
        yield skill


def get_stats_of_class():
    logger.info(f'Getting stats')

    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))
    kwargs = {}
    for i, row in enumerate(table.find_elements(By.CSS_SELECTOR, f'tr'), start=1):
        if 5 <= i <= 11:
            row_name = unicodedata.normalize('NFKD',
                            row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
                            .get_attribute("innerText"))
            logger.info(row_name)
            row_name = re.search(r"(MAX\s*HP|DODGE|PROT|SPD|ACC\s*MOD|CRIT|DMG)", row_name, re.I).group()
            row_name = re.sub(r'\s+', '_', row_name).lower()
            values_obtaining_function, value_modifying_function = \
                character_level_kwargs[row_name]

            values = values_obtaining_function(row)
            values = [value_modifying_function(value) for value in values]
            kwargs[row_name] = values

        logger.debug(f'kwargs:\n{pformat(kwargs)}')

    for i in range(5):
        new_kwargs = {attribute_name: values[i] for attribute_name, values in kwargs.items()}
        new_model = CharacterLevelModel(**new_kwargs)
        logger.debug(new_model)
        yield new_model


def insert_into_table(table_name: str, attributes: tuple, values_list: [tuple], con, cur):
    logger.info(pformat(table_name))
    logger.info(pformat(attributes))
    logger.info(pformat(values_list))
    query = f'BEGIN TRANSACTION;' \
            f'INSERT INTO "{table_name}"('

    col_names = [f'"{attribute}"' for attribute in attributes]
    query += ','.join(col_names) + f') VALUES ('

    for values in iter(values_list):
        values_for_entity = []
        for value in iter(values):
            new_value = value
            if new_value is None:
                new_value = "NULL"
            elif type(new_value) is str:
                new_value = f'"{new_value}"'
            values_for_entity.append(new_value)
        query += ','.join(values_for_entity) + f'), ('

    query.rstrip(', (') + ';COMMIT;'

    logger.info(query)
    cur.execute(query)
    con.commit()


def get_db_cursor():
    con = sqlite3.connect("darkest_dungeon.db")
    return con, con.cursor()


def setup_logger():
    # get the multiprocessing logger
    logger = logging.getLogger()
    # configure a stream handler
    formatter = logging.Formatter("[%(asctime)s:%(levelname)7s:%(filename)s:%(lineno)s:%(funcName)s()] %(message)s")

    file_handler = logging.FileHandler(os.path.join(os.getcwd(),
                                                    f'log_{datetime.datetime.now().strftime("%d_%b_%y_%H_%M_%S")}.log'),
                                       encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)
    # log all messages, debug and up
    return logger

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('log-level=OFF')
    service = Service(ChromeDriverManager(path=r"C:\Users\edu_a\.virtualenvs\darkest_dungeon-IEFPBDCG\src").install())

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    return driver, wait, actions


def get_characters_with_effects(_characters: [CharacterModel], patterns: [re.Pattern]):
    for pattern in patterns:
        yield get_characters_with_effect(_characters, pattern)


def get_characters_with_effect(_characters: [CharacterModel], pattern: re.Pattern):
    def _get_skills_with_effect(_skills: [SkillModel], _pattern: re.Pattern):
        for skill in iter(_skills):
            for effect in iter(skill.effects):
                if _pattern.search(effect.description):
                    yield skill

    for character in iter(_characters):
        skills = [skill for skill in _get_skills_with_effect(character.skills, pattern)]
        if len(skills) > 0:
            yield CharacterModel(character.class_name, skills)


def get_character_details(class_name):
    parsed = re.sub(r' ', '_', class_name)
    url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
    driver.get(url)
    skills = [skill for skill in get_skills()]
    stats = [stat for stat in get_stats_of_class()]
    return stats, skills


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger = setup_logger()
    driver, wait, actions = setup_driver()
    con, cur = get_db_cursor()

    try:
        characters = [character for character in get_characters()]
        for character in iter(characters):
            stats, skills = get_character_details(character.name)
            character.add_skills(skills) \
                .add_stats(stats)

        logger.debug(f'Character list:')
        for c in characters:
            n_skills = len(c.skills)
            logger.debug(f'{c.name} with {n_skills} skills:\n{pformat(c)}')
            assert n_skills >= 7

        # insert_into_table('Character', con, cur)

        # effects = [e.value for e in list(Effects)]
        # for i, effect in enumerate(iter(effects)):
        #     logger.debug(f'################ Characters with effect {list(Effects)[i].name}:')
        #     logger.debug(f'###################################################')
        #     for character in get_characters_with_effect(characters, effect):
        #         logger.info(pformat(character))



    except Exception as e:
        logger.error(traceback.format_exc())
        driver.quit()
        exit(1)

    driver.quit()
    exit(0)
