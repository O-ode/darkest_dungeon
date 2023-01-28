import multiprocessing as mp
import re

from constants import OpenQuotesEnum
from repos.daos.text_reader_daos.file_class import FileClass

logger = mp.get_logger()


class TextReaderDao:

    @classmethod
    def _edit_line(cls, line):
        new_line = []
        flag = OpenQuotesEnum(0)
        for char in line[:-1]:
            if char == '\'':
                flag ^= OpenQuotesEnum.SINGLE
                continue
            elif char == '"':
                flag ^= OpenQuotesEnum.DOUBLE
                continue
            elif char == ' ':
                if flag.value != 0:
                    char = '_'
            new_line.append(char)
        return ''.join(new_line)

    @classmethod
    def _log_match(cls, match: re.Match):
        if match.lastgroup == 'attr_name':
            s = '\t'
        elif match.lastgroup == 'attr_value':
            s = '\t\t'
        else:
            s = ''
        s += f'{match.lastgroup}: {repr(match.group(match.lastgroup))}'
        # logger.debug(s)

    @classmethod
    def extract_values_from_file(cls, file: FileClass) -> list[tuple[str, dict[str, list[str]]]]:

        with open(file.get_absolute_path(), 'r') as game_file:
            for line in game_file:
                row_attrs = {}
                last_attr_name = ''
                values = []
                regexes = [
                    re.compile(r'(?P<row_name>\w+):'),
                    re.compile(r'(?<!\d)\.(?P<attr_name>\w+)'),
                    re.compile(r'(?P<attr_value>\S+)')
                ]
                full_string = '|'.join(r.pattern for r in regexes)
                full_regex = re.compile(fr'{full_string}')

                new_line = cls._edit_line(line)

                for match in full_regex.finditer(new_line):
                    cls._log_match(match)
                    group = match.group(match.lastgroup)
                    if match.lastgroup == 'row_name':
                        row_name = group
                    elif match.lastgroup == 'attr_name':
                        if last_attr_name != '':
                            row_attrs[last_attr_name] = values
                            values = []
                        last_attr_name = group
                    elif match.lastgroup == 'attr_value':
                        values.append(group)
                row_attrs[last_attr_name] = values

                yield row_name, row_attrs
