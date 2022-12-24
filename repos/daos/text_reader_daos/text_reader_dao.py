import logging
import re

from repos.daos.text_reader_daos.constants import DARKEST_ROOT_FOLDER

logger = logging.getLogger()


class TextReaderDao:

    @classmethod
    def file_to_dict(cls, relative_path: str, file_name: str):
        dict_values = {}
        logger.debug([DARKEST_ROOT_FOLDER, relative_path, file_name])
        full_path = "\\".join([DARKEST_ROOT_FOLDER, relative_path, file_name])
        with open(full_path, 'r') as game_file:
            for line in game_file:
                line_content = re.split(r':\s|\s?(?<!\w)\.', line)
                row_name = line_content[0]
                dict_values[row_name] = {}
                for text in iter(line_content[2:]):
                    split = re.split(r'\s', text)
                    split = [e for e in split if e != '']
                    if len(split) == 2:
                        dict_values[row_name][split[0]] = split[1]
                    else:
                        dict_values[row_name][split[0]] = split[1:]

        return dict_values
