import logging
import sqlite3

from constants import pretty

logger = logging.getLogger()


class DBManager:

    def __init__(self):
        self.con = sqlite3.connect("darkest_dungeon.db")
        self.cur = self.con.cursor()

    def get_db_con_cursor(self):
        return self.con, self.cur

    def insert_into_table(self, table_name: str, attributes: tuple, values_list: [tuple]):
        logger.info(pretty(table_name))
        logger.info(pretty(attributes))
        logger.info(pretty(values_list))
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
        self.cur.execute(query)
        self.con.commit()
