import re

from source.enums.matrix import GitHub, Sheets
from source.enums.path import Path
from source.matrix.allure_parser import ParserJSON
from source.matrix.git_parser import GitHubAPI
from source.matrix.sheets import SheetsAPI

if __name__ == "__main__":
    try:
        for service in GitHub.SERVICES.value:
            sheets = SheetsAPI(credentials_info=Sheets.CREDENTIALS.value, spreadsheet_id=Sheets.SPREADSHEET_ID)
            existing_test_cases = sheets.get_all_rows_in_column(sheet=service, column="B2:B")

            """Сбор актуальных автотестов и запись в матрицу покрытия"""
            gh_pages = GitHubAPI(owner=GitHub.OWNER, repository=GitHub.REPO_TESTS, token=GitHub.TOKEN)

            folder_names = gh_pages.get_all_name_folder(branch=GitHub.BRANCH_GH)
            last_report = max(int(s) for s in folder_names if s.isdigit())

            parser = ParserJSON()
            file_allure = parser.open_json_file(Path.ALLURE_REPORT.value)
            test_cases_allure = parser.extract_test_cases(file_allure)
            pattern_allure_links = f"https://{GitHub.OWNER}.github.io/{GitHub.REPO_TESTS}/{last_report}/#behaviors/"

            allure_report = [
                {
                    'id': item['name'].split(" ")[0],
                    'name': item['name'],
                    'link': f"{pattern_allure_links}{item['parentUid']}/{item['uid']}/"
                }
                for item in test_cases_allure
                if re.match(pattern="^T[A-Z]\d+", string=item['name'])
            ]

            sheets.append_hyperlinks_for_id(sheet=service, id_column="A2:A", column="C2:C",
                                            new_test_cases=allure_report)

            print(f"Данные успешно добавлены")
    except Exception as e:
        print(f"Данные не удалось обновить\n{str(e)}")
