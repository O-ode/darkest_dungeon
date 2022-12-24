import logging
from typing import Any

from repos.daos.text_reader_daos.text_reader_dao import TextReaderDao

logger = logging.getLogger()


class FileClass:
    def __init__(self, relative_path: str, name: str, file_values: dict = None):
        self.relative_path = relative_path
        self.name = name
        self.file_values: dict or None = file_values

    def get_absolute_path(self):
        return r'\\'.join([self.relative_path, self.name])

    def __eq__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self.name == other.name:
                return self.relative_path == other.relative_path
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self.relative_path < other.relative_path:
                return True
            elif self.relative_path > other.relative_path:
                return False
            else:
                if self.name < other.name:
                    return True
                else:
                    return False

    def __gt__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self.relative_path > other.relative_path:
                return True
            elif self.relative_path < other.relative_path:
                return False
            else:
                if self.name > other.name:
                    return True
                else:
                    return False


class FileRepo:
    files: [FileClass] = []

    @classmethod
    def get_dict_from_file(cls, relative_path: str, name: str):
        target_file = FileClass(relative_path, name)
        if len(cls.files) > 0:
            result, index = cls.find_in_list_merge_recursively(cls.files, target_file)
        else:
            result, index = None, 0
        if result is None:
            target_file.file_values = TextReaderDao.file_to_dict(relative_path, name)
            if len(cls.files) == index:
                cls.files.append(target_file)
            else:
                cls.files.insert(index, result)
        return target_file.file_values

    @classmethod
    def find_in_list_merge_recursively(cls, arr: list, target: Any, steps=0, target_index=0) -> tuple[Any or None, int]:
        steps += 1
        index = len(arr) // 2
        current = arr[index]
        logger.debug(f'step: {steps}, index: {index}, target_index: {target_index}, current: {current}, '
                     f'target:{target}, arr: {arr[0]}..{arr[-1]}')
        if target == current:
            target_index += index
            logger.debug(f"Found target! {current}, steps given: {steps}")
            return current, target_index
        elif target > current:
            if arr[0] == arr[-1]:
                return None, target_index + 1
            target_index += index
            return cls.find_in_list_merge_recursively(arr[index:], target, steps, target_index)
        else:
            if arr[0] == arr[-1]:
                return None, target_index
            return cls.find_in_list_merge_recursively(arr[:index], target, steps, target_index)
