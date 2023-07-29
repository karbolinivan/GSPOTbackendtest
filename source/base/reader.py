from pandas import read_excel


class Reader:
    def __init__(self, path_file, sheet):
        self.sheet = sheet
        self.path = path_file

    def get_data(self, id_test: str):
        file = read_excel(self.path, sheet_name=self.sheet)
        test_data = file[file["id"] == id_test].to_dict(orient="records")
        return test_data[0] if test_data else None
