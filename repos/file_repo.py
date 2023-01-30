import multiprocessing as mp
import os
from typing import Any

from repos.daos.text_reader_daos.constants import DARKEST_ROOT_FOLDER
from repos.daos.text_reader_daos.file_class import FileClass
from repos.daos.text_reader_daos.text_reader_dao import TextReaderDao

logger = mp.get_logger()


class FileRepo:
    _hero_files: list[FileClass] = []
    _monster_files: list[FileClass] = []

    @classmethod
    def get_enemy_files(cls) -> list[FileClass]:
        monsters_folders = [r'monsters', r'dlc\735730_color_of_madness\monsters']
        monsters_folders_paths = [fr'{DARKEST_ROOT_FOLDER}\{folder}' for folder in monsters_folders]
        cls._monster_files.extend(
            (FileClass(file, path) for path in monsters_folders_paths for file in os.listdir(path))
        )
        return cls._monster_files

    @classmethod
    def get_file(cls, relative_path: str, name: str):
        search_file = FileClass(relative_path, name)
        # logger.info(f'Getting file {search_file}')
        result, index = cls.find_in_list_merge_recursively(cls._hero_files, search_file)
        if result is None:
            cls._add_file(search_file, index)
            result = search_file
        return result

    @classmethod
    def _add_file(cls, search_file: FileClass, index: int):
        for row_values in TextReaderDao.extract_values_from_file(search_file):
            # logger.debug(f'Adding row values: {pretty(row_values)}')
            search_file.add_file_values(row_values)

        if len(cls._hero_files) == index:
            cls._hero_files.append(search_file)
        else:
            cls._hero_files.insert(index, search_file)

    @classmethod
    def get_file_values_by_key(cls, key: str, relative_path: str, name: str):
        file_values = cls.get_file(relative_path, name).get_file_values()
        for row_name, row_values in file_values:
            if row_name == key:
                yield row_values

    @classmethod
    def find_in_list_merge_recursively(cls, a_list: list, a_target: Any, **kwargs) -> tuple[Any, int]:

        def _find_in_list_merge_recursively(arr: list, target: Any, steps=0, target_index=0) -> tuple[Any, int]:
            steps += 1
            index = len(arr) // 2
            current = arr[index]
            # logger.debug(f'step: {steps}, index: {index}, target_index: {target_index}, current: {current}, '
            #              f'target:{target}, arr: {arr[0]}..{arr[-1]}')

            # stopping conditions
            if target == current:
                target_index += index
                logger.debug(f"Found target! {current}, steps given: {steps}")
            elif arr[0] == arr[-1]:
                if target > current:
                    target_index += 1
                current = None

            else:
                if target > current:
                    target_index += index
                    split_arr = arr[index:]
                else:
                    split_arr = arr[:index]
                return _find_in_list_merge_recursively(split_arr, target, steps, target_index)

            return current, target_index

        if len(a_list) != 0:
            return _find_in_list_merge_recursively(a_list, a_target, **kwargs)
        else:
            return None, 0
