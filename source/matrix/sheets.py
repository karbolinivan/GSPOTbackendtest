import os
import re

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google.oauth2.gdch_credentials import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from source.enums.matrix import Sheets


class SheetsAPI:
    def __init__(self, credentials_info, spreadsheet_id, token_path=None, scopes=None, ):
        self.credentials = None
        self.token = token_path
        self.scopes = scopes
        self.spreadsheet_id = spreadsheet_id
        self.credentials_info = credentials_info
        self.service = self.connection()

    def connection(self):
        try:
            self.credentials = service_account.Credentials.from_service_account_info(
                self.credentials_info)
            service = build("sheets", "v4", credentials=self.credentials)
            return service
        except Exception as e:
            print(f"Нет подключения\n{e}")

    def append_text(self, sheet, column, values):
        range_name = f"{sheet}!{column}"
        body = {"values": values}
        self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id, range=range_name,
            valueInputOption="RAW", insertDataOption="INSERT_ROWS", body=body
        ).execute()

    @classmethod
    def _find_max_id(cls, current_id):
        max_id = 0
        for item in current_id:
            match = re.search(r'\d+', item)
            if match:
                id_value = int(match.group())
                max_id = max(max_id, id_value)
        return max_id

    def _generate_id(self, sheet, pattern_id, id_column, amount):

        if amount == 0:
            return []

        id_range_name = f"{sheet}!{id_column}"
        id_result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=id_range_name,
            valueRenderOption="FORMULA"
        ).execute()

        current_id = [item[0] for item in id_result.get("values", [])]

        new_list = [[f"{pattern_id}{self._find_max_id(current_id=current_id) + i}"] for i in range(1, amount + 1)]

        return new_list

    def add_new_id(self, sheet, id_column, id_list):
        range_name = f"{sheet}!{id_column}"
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name
        ).execute()
        last_row = len(values.get("values", [])) + 2
        new_range = re.sub(r'\d+', repl=str(last_row), string=range_name)

        body = {
            "values": id_list
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=new_range,
            valueInputOption="USER_ENTERED", body=body
        ).execute()

    def append_text_with_hyperlink_by_id(self, sheet, column, id_column, pattern_id, test_cases):
        range_name = f"{sheet}!{column}"

        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name
        ).execute()

        last_row = len(values.get("values", [])) + 2
        new_range = re.sub(r'\d+', repl=str(last_row), string=range_name)
        new_test_cases = [[f'=HYPERLINK("{item["link"]}"; "{item["name"]}")'] for item in test_cases]

        body = {
            "values": new_test_cases
        }

        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=new_range,
            valueInputOption="USER_ENTERED", body=body
        ).execute()

        new_id_list = self._generate_id(
            sheet=sheet, id_column=id_column, pattern_id=pattern_id, amount=len(new_test_cases)
        )
        self.add_new_id(sheet=sheet, id_column=id_column, id_list=new_id_list)

    def get_all_rows_in_column(self, sheet, column):
        range_name = f"{sheet}!{column}"
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name
        ).execute()

        values_column = result.get('values', [])
        filled_rows = []
        for row_num, row in enumerate(values_column, start=1):
            if row:
                filled_rows.append(row[0])

        return filled_rows

    def get_all_rows_in_column_with_hyperlink(self, sheet, column):
        range_name = f"{sheet}!{column}"
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name,
            valueRenderOption="FORMULA"
        ).execute()

        values_column = result.get('values', [])
        filled_rows = []

        for row_num, row in enumerate(values_column, start=1):
            if row:
                cell_value = row[0]
                hyperlink_parts = cell_value.split('"')

                if len(hyperlink_parts) >= 3:
                    hyperlink = hyperlink_parts[1]
                    text = hyperlink_parts[3]
                    filled_rows.append({'name': text, 'link': hyperlink})

        return filled_rows

    def get_all_rows_with_hyperlink_and_id(self, sheet, column, id_column):
        try:
            range_name = f"{sheet}!{column}"
            id_range_name = f"{sheet}!{id_column}"

            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id, range=range_name,
                valueRenderOption="FORMULA"
            ).execute()

            id_result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id, range=id_range_name,
                valueRenderOption="FORMULA"
            ).execute()

            values_column = result.get('values', [])
            id_values_column = id_result.get('values', [])
            filled_rows = []

            for row_num, row in enumerate(values_column, start=1):
                if row and row[0]:
                    cell_value = row[0]
                    hyperlink_parts = cell_value.split('"')

                    if len(hyperlink_parts) >= 3:
                        hyperlink = hyperlink_parts[1]
                        text = hyperlink_parts[3]

                        if row_num <= len(id_values_column):
                            id_value = id_values_column[row_num - 1][0]
                            filled_rows.append({'id': id_value, 'name': text, 'link': hyperlink})
                        else:
                            filled_rows.append({'id': None, 'name': text, 'link': hyperlink})

            return filled_rows
        except Exception as e:
            print(f"Данные не были получены\n{e}")

    def append_hyperlinks_for_id(self, sheet, id_column, column, new_test_cases):
        range_name_id = f"{sheet}!{id_column}"
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=range_name_id
        ).execute()
        values = result.get('values', [])

        id_to_data_mapping = {item["id"]: {"link": item["link"], "name": item["name"]} for item in new_test_cases}

        column_values = []

        for row in values:
            if row and row[0] in id_to_data_mapping:
                id_value = row[0]
                data = id_to_data_mapping[id_value]
                link = data["link"]
                name = data["name"]
                hyperlink_formula = f'=HYPERLINK("{link}"; "{name}")'
                column_values.append([hyperlink_formula])
            else:
                column_values.append([""])

        range_name_test = f"{sheet}!{column}"

        body = {"values": column_values}
        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=range_name_test,
            valueInputOption="USER_ENTERED", body=body
        ).execute()

    def remove_empty_rows_by_name(self, sheet, column):
        sheet_info = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
        sheets = sheet_info.get('sheets', [])

        target_sheet_id = None
        for sheet_info in sheets:
            if sheet_info['properties']['title'] == sheet:
                target_sheet_id = sheet_info['properties']['sheetId']
                break

        if target_sheet_id is not None:
            range_name = f"{sheet}!{column}"
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id, range=range_name,
                valueRenderOption="FORMULA"
            ).execute()

            values_column = result.get('values', [])
            rows_to_delete = []

            for row_num, row in enumerate(values_column, start=2):
                if not row or not row[0]:
                    rows_to_delete.append(row_num)

            if rows_to_delete:
                for row in reversed(rows_to_delete):
                    self.service.spreadsheets().batchUpdate(
                        spreadsheetId=self.spreadsheet_id,
                        body={
                            "requests": [
                                {
                                    "deleteDimension": {
                                        "range": {
                                            "sheetId": target_sheet_id,
                                            "dimension": "ROWS",
                                            "startIndex": row - 1,
                                            "endIndex": row
                                        }
                                    }
                                }
                            ]
                        }
                    ).execute()
        else:
            print(f"Лист '{sheet}' не найден.")

    def remove_rows_not_in_list_by_name(self, sheet, column, actual_cases):
        sheet_info = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
        sheets = sheet_info.get('sheets', [])

        target_sheet_id = None
        for sheet_info in sheets:
            if sheet_info['properties']['title'] == sheet:
                target_sheet_id = sheet_info['properties']['sheetId']
                break

        if target_sheet_id is not None:
            range_name = f"{sheet}!{column}"
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id, range=range_name,
                valueRenderOption="FORMULA"
            ).execute()

            values_column = result.get('values', [])
            rows_to_delete = []

            for row_num, row in enumerate(values_column, start=2):
                if row:
                    cell_value = row[0]
                    hyperlink_parts = cell_value.split('"')

                    if len(hyperlink_parts) >= 3:
                        text = hyperlink_parts[3]
                        if text not in actual_cases:
                            rows_to_delete.append(row_num)

            if rows_to_delete:
                for row in reversed(rows_to_delete):
                    self.service.spreadsheets().batchUpdate(
                        spreadsheetId=self.spreadsheet_id,
                        body={
                            "requests": [
                                {
                                    "deleteDimension": {
                                        "range": {
                                            "sheetId": target_sheet_id,
                                            "dimension": "ROWS",
                                            "startIndex": row - 1,
                                            "endIndex": row
                                        }
                                    }
                                }
                            ]
                        }
                    ).execute()
        else:
            print(f"Лист '{sheet}' не найден.")


sheets = SheetsAPI(credentials_info=Sheets.CREDENTIALS.value, spreadsheet_id=Sheets.SPREADSHEET_ID)
