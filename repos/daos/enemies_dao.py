import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from driver_singleton import DriverSingleton
from factories.web_element_value_factory import WebElementValueFactory

ENEMIES_LIST_URL = r"https://darkestdungeon.fandom.com/wiki/Enemies_(Darkest_Dungeon)"


class EnemiesDAO:
    @classmethod
    def get_enemies_per_region(cls):
        for list_name_element, enemies_elements_list in EnemiesSeleniumDAO.get_enemies_names():
            list_name = re.search(
                r'(?<=List of )\w+( Bosses)?(?=Monsters)?',
                WebElementValueFactory.str_text_from_inner_text(list_name_element)
            )
            enemies_names = [WebElementValueFactory.str_text_from_inner_text(e) for e in enemies_elements_list]
            yield list_name, enemies_names


class EnemiesSeleniumDAO:

    @classmethod
    def get_enemies_names(cls):
        if DriverSingleton.get_driver().current_url != ENEMIES_LIST_URL:
            DriverSingleton.get_driver().get(ENEMIES_LIST_URL)
        try:
            DriverSingleton.get_wait().until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
        except:
            pass

        DriverSingleton.get_wait().until(EC.presence_of_element_located(
            (By.XPATH, f'//*[text()="List of Shared Monsters"]'))
        )

        container = DriverSingleton.get_driver().find_element(By.CSS_SELECTOR, 'div.mw-parser-output')

        enemies_tables = container.find_elements(By.CSS_SELECTOR, 'table.wikitable')[3:]
        names_list = container.find_elements(By.CSS_SELECTOR, 'h2')

        yield from [(list_name_element, enemy_table.find_elements(
            By.CSS_SELECTOR, 'tbody > tr > td:nth-child(1) > a:nth-child(3)'
        )) for list_name_element, enemy_table in zip(names_list, enemies_tables)]