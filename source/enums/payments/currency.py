from enum import Enum

class Currencies(str, Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"

    def __str__(self) -> str:
        return self.value