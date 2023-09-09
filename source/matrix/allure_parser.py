import json


class ParserJSON:
    def __init__(self):
        self.file = None

    def open_json_file(self, path):
        with open(path, 'r') as json_file:
            self.file = json.load(json_file)
        return self.file

    def extract_test_cases(self, data, parent_uid=None):
        test_cases = []
        if 'children' in data:
            for child in data['children']:
                test_cases += self.extract_test_cases(child, parent_uid=data.get('uid'))
        if 'uid' in data and 'name' in data:
            test_cases.append({
                'uid': data['uid'],
                'name': data['name'],
                'parentUid': parent_uid
            })
        return test_cases
