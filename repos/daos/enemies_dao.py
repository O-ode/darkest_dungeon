import warnings

ENEMIES_LIST_URL = r"https://darkestdungeon.fandom.com/wiki/Enemies_(Darkest_Dungeon)"

warnings.warn("File to be updated", DeprecationWarning)


class EnemiesDAO:
    @classmethod
    def get_enemies_per_region(cls):
        # for list_name_element, enemies_elements_list in EnemiesSeleniumDAO.get_enemies_names():
        #     list_name = re.search(
        #         r'(?<=List of )\w+( Bosses)?(?=Monsters)?',
        #         WebElementValueFactory.str_text_from_inner_text(list_name_element)
        #     )
        #     enemies_names = [WebElementValueFactory.str_text_from_inner_text(e) for e in enemies_elements_list]
        #     yield list_name, enemies_names
        pass
