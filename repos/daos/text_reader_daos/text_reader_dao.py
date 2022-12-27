import multiprocessing as mp
import re

from repos.daos.text_reader_daos.file_class import FileClass

logger = mp.get_logger()


class TextReaderDao:

    @classmethod
    def extract_values_from_file(cls, file: FileClass) -> list[dict]:

        with open(file.get_absolute_path(), 'r') as game_file:
            for line in game_file:
                line_content = re.split(r':\s\.|\s+\.', line[:-1])
                line_attributes_iter = iter(line_content)
                row_name = next(line_attributes_iter)  # name of the row goes first
                row_values = {row_name: [attr_and_values_str for attr_and_values_str in line_attributes_iter]}
                yield row_values
