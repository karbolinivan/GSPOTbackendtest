from enum import Enum
from source.base.reader import Reader
from source.enums.path import Path

reader = Reader(path_file=Path.TEST_DATA, sheet="Games")


class GamesData(Enum):
    TG1 = reader.get_data(id_test="TG1")
    TG2 = reader.get_data(id_test="TG2")

    def __str__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]
