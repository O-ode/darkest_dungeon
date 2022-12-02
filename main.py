import datetime
import logging
import os.path
import traceback
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from character_functions import SeleniumCharacterManager
from constants import pretty


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


def setup_logger():
    # get the multiprocessing logger
    logger = logging.getLogger()
    # configure a stream handler
    formatter = logging.Formatter("[%(asctime)s:%(levelname)7s:%(filename)s:%(lineno)s:%(funcName)s()] %(message)s")

    file_handler = logging.FileHandler(os.path.join(os.getcwd(),
                                                    f'log_{datetime.datetime.now().strftime("%d_%b_%y_%H_%M_%S")}.log'),
                                       encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
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
    options.add_argument('log-level=3')
    service = Service(ChromeDriverManager(path=r"C:\Users\edu_a\.virtualenvs\darkest_dungeon-IEFPBDCG\src").install())
    _driver = webdriver.Chrome(service=service, options=options)

    _wait = WebDriverWait(_driver, 10)
    _actions = ActionChains(_driver)
    return _driver, _wait, _actions


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger = setup_logger()
    driver, wait, actions = setup_driver()

    try:
        seleniumCharacterManager = SeleniumCharacterManager(driver, wait)
        characters = [c for c in seleniumCharacterManager.get_characters()]
        seleniumCharacterManager.fetch_characters_details(characters)

        logger.info(f'Character list:')
        for c in characters:
            n_skills = len(c.skills)
            logger.info(f'{c.name} with {n_skills} skills:\n{pretty(c)}')
            assert n_skills >= 7

    except:
        logger.error(traceback.format_exc())
        driver.quit()
        sleep(30)
        exit(1)

    driver.quit()
    exit(0)
