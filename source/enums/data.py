import json
from enum import Enum
from source.base.reader import Reader
from source.enums.path import Path

reader_games = Reader(path_file=Path.TEST_DATA, sheet="Games")


class Cases(Enum):
    GAMES = reader_games.get_dict_excel()

    def __str__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    @staticmethod
    def get_parametrize(test_case: str):
        return (
            Cases.GAMES[f"{test_case}"]["id"], Cases.GAMES[f"{test_case}"]["name"], Cases.GAMES[f"{test_case}"]["link"],
            Cases.GAMES[f"{test_case}"]["test_data"])
