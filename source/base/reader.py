from pandas import read_csv


class Reader:
    def __init__(self, path_file):
        self.path = path_file
        self.file = read_csv(self.path, sep=";", encoding="utf-8")

    def _read_data_from_csv(self, id_test: str):
        test_data = self.file[self.file["id"] == id_test].to_dict(orient="records")
        return test_data[0] if test_data else None

    def _get_amount_rows(self, title: str):
        return self.file[title].count()

    def get_dict_csv(self):
        keys = [f"TG{x}" for x in range(1, self._get_amount_rows(title='id') + 1)]
        values = [self._read_data_from_csv(id_test=f"TG{x}") for x in range(1, self._get_amount_rows(title='id') + 1)]
        return {k: v for k, v in zip(keys, values)}
