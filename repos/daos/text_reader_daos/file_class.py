from repos.daos.text_reader_daos.constants import DARKEST_ROOT_FOLDER


class FileClass:
    def __init__(self, relative_path: str, name: str):
        self._relative_path: str = relative_path
        self._name: str = name
        self._file_values: list[tuple[str, dict[str, list[str]]]] = []

    def get_file_values(self) -> list[tuple[str, dict[str, list[str]]]]:
        return self._file_values

    def get_relative_path(self) -> str:
        return self._relative_path

    def get_name(self) -> str:
        return self._name

    def get_absolute_path(self):
        return '\\'.join([DARKEST_ROOT_FOLDER, self._relative_path, self._name])

    def add_file_values(self, row_tuple: tuple[str, dict[str, list[str]]]):
        self._file_values.append(row_tuple)

    def __eq__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self._name == other._name:
                return self._relative_path == other._relative_path
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self._relative_path < other._relative_path:
                return True
            elif self._relative_path > other._relative_path:
                return False
            else:
                if self._name < other._name:
                    return True
                else:
                    return False

    def __gt__(self, other):
        if other is not None and isinstance(other, self.__class__):
            if self._relative_path > other._relative_path:
                return True
            elif self._relative_path < other._relative_path:
                return False
            else:
                if self._name > other._name:
                    return True
                else:
                    return False

    def __repr__(self):
        return f'{self._relative_path}\\{self._name}'
