import os
from enum import Enum


class Path(str, Enum):
    GAMES_DB = "../../source/database/games/.env"
    ALLURE_REPORT = os.path.abspath(os.path.join(os.getcwd(), "../../allure-report/data/behaviors.json"))

    def __str__(self) -> str:
        return self.value
