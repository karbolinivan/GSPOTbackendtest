from enum import Enum
from source.base.reader import Reader
from source.enums.path import Path

reader_games = Reader(path_file=Path.GAMES_CSV)


class Cases(Enum):
    GAMES = reader_games.get_dict_csv()
    PAYMENTS = ""

    def __str__(self):
        return self.value

    def __getitem__(self, key):
        return self.value[key]

    @classmethod
    def get_parametrize(cls, service: str, test_case: str):
        if service.lower() == "games":
            service_data = cls.GAMES
        elif service.lower() == "payments":
            service_data = cls.PAYMENTS
        else:
            raise ValueError(f"Unknown service: {service}")
        data = service_data[test_case]
        return data["id"], data["name"], data["link"], data["test_data"]
