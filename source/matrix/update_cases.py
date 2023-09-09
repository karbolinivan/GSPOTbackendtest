import os

from source.enums.matrix import GitHub, Sheets
from source.matrix.git_parser import GitHubAPI
from source.matrix.sheets import SheetsAPI

print(Sheets.CREDENTIALS.value)
print(GitHub.TOKEN.value)
if __name__ == "__main__":
    try:
        for service in GitHub.SERVICES.value:
            """Добавление актуальных тест-кейсов из документации в матрицу покрытия"""
            documentation_repository = GitHubAPI(
                owner=GitHub.OWNER.value, repository=GitHub.REPO_DOCS.value, token=GitHub.TOKEN.value
            )
            git_test_cases = documentation_repository.get_all_test_case_from_directory(directory=service.lower())

            sheets = SheetsAPI(credentials_info=Sheets.CREDENTIALS.value, spreadsheet_id=Sheets.SPREADSHEET_ID)
            existing_test_cases = sheets.get_all_rows_in_column(sheet=service, column="B2:B")

            new_test_cases = [
                {"name": item['name'], "link": item["link"]}
                for item in git_test_cases
                if item["name"] not in existing_test_cases
            ]

            if service == "Games":
                pattern_id = "TG"
            elif service == "Payments":
                pattern_id = "TP"
            elif service == "Channel":
                pattern_id = "TC"
            else:
                pattern_id = "TU"

            actual_name_cases = [
                item["name"]
                for item in git_test_cases
            ]

            sheets.remove_empty_rows_by_name(sheet=service, column="B2:B")

            sheets.remove_rows_not_in_list_by_name(sheet=service, column="B2:B", actual_cases=actual_name_cases)

            sheets.append_text_with_hyperlink_by_id(
                sheet="Games", column="B2:B", id_column="A2:A", pattern_id=pattern_id, test_cases=new_test_cases
            )

            print(f"Данные успешно добавлены")
    except Exception as e:
        print(f"Данные не удалось обновить\n{str(e)}")
