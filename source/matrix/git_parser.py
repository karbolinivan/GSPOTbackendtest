import requests


class GitHubAPI:
    def __init__(self, owner, repository, token):
        self.headers = {'Authorization': f'token {token}'}
        self.url = f'https://api.github.com/repos/{owner}/{repository}/contents/'
        self.params = None

    def _get_file_info(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return [
                {'name': item['name'], 'url': item['html_url']}
                for item in response.json()
                if item['type'] == 'file']
        return []

    def _traverse_directory(self, directory_url):
        file_info = self._get_file_info(directory_url)

        result_list = []

        for file_data in file_info:
            if file_data['name'] not in ['README.MD', '.gitkeep', "README.md"]:
                result_list.append({"name": file_data['name'].split(".")[0], "link": file_data["url"]})

        subdirs_url = [item['url'] for item in self._get_file_contents(directory_url) if item['type'] == 'dir']
        for subdir_url in subdirs_url:
            subdir_results = self._traverse_directory(subdir_url)
            result_list.extend(subdir_results)

        return result_list

    def _get_file_contents(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return []

    def get_all_test_case_from_directory(self, directory):
        url_service = f"{self.url}{directory}"
        return self._traverse_directory(directory_url=url_service)

    def get_all_name_folder(self, branch):
        params = {
            'ref': branch
        }

        response = requests.get(url=self.url, headers=self.headers, params=params)

        if response.status_code == 200:
            data = response.json()
            folder_names = [item['name'] for item in data if item['type'] == 'dir']
            return folder_names
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
            return []
