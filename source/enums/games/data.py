from enum import Enum
from source.base.reader import Reader
from source.enums.path import Path

reader = Reader(path_file=Path.TEST_DATA, sheet="Games")


class Games(Enum):
    CASES = reader.get_dict()

    def __str__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]
