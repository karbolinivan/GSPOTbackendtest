from enum import Enum


class Path(str, Enum):
    GAMES = "../../source/database/games/.env"

    def __str__(self) -> str:
        return self.value
