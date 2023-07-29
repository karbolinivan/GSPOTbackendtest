import os
from enum import Enum


class Path(str, Enum):
    GAMES_DB = "../../source/database/games/.env"
    TEST_DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data.xlsx"))

    def __str__(self) -> str:
        return self.value
