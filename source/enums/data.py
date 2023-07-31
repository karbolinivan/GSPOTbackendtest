from enum import Enum
from source.base.reader import Reader
from source.enums.path import Path

reader_games = Reader(path_file=Path.GAMES_CSV)


class Cases(Enum):
    GAMES = reader_games.get_dict_csv()

    def __str__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    @staticmethod
    def get_parametrize(test_case: str):
        data = Cases.GAMES[f"{test_case}"]
        return data["id"], data["name"], data["link"], data["test_data"]
