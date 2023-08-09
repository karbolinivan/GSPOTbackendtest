import os
from enum import Enum


class Path(str, Enum):
    GAMES_DB = "../../source/database/games/.env"
    GAMES_CSV = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data/games.csv"))

    def __str__(self) -> str:
        return self.value
