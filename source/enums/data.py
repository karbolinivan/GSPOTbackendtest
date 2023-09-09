from enum import Enum
from source.matrix.sheets import sheets

cases_games = sheets.get_all_rows_with_hyperlink_and_id(sheet="Games", column="B2:B", id_column="A2:A")


class Cases(Enum):
    GAMES = {f"{item['id']}": item for item in cases_games} if cases_games else None
    PAYMENTS = ""
    TG77 = {
        "name": "qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop"
    }
    TG78 = {
        "name": "qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopA"
    }
    TG88 = {"name": "e"}
    TG90 = {"name": ""}
    TG82 = {"name": "1234567890"}
    TG83 = {"name": "  "}
    TG84 = {"name": "下来顔文字"}
    TG85 = {"name": "Հայկականتحتاجفقطإلىنسخלבדוק"}
    TG86 = {"name": "Ru En"}
    TG89 = {"name": "!@#$%^&*()_+=-"}
    TG79 = {"name": " ru"}
    TG80 = {"name": "ru "}
    TG87 = {"name": "Ru En"}
    TG99 = {"name": "  "}
    TG100 = {"name": ""}

    def __getitem__(self, key):
        if self.value is None:
            return {'id': 'None', 'name': 'None', 'link': 'None'}
        return self.value.get(key, {'id': 'None', 'name': 'None', 'link': 'None'})

    def __str__(self):
        return self.value
