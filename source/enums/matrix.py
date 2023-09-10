import json
import os
from enum import Enum


class GitHub(Enum):
    OWNER = 'karbolinivan'
    REPO_DOCS = 'GSPOTtestingdocumentation'
    REPO_TESTS = "GSPOTbackendtest"
    TOKEN = os.environ.get('GITHUB_PARSER')
    SERVICES = ["Games"]
    BRANCH_GH = "gh-pages"

    def __str__(self):
        return self.value


class Sheets(Enum):
    SPREADSHEET_ID = "1s0f-YtiR_4uCymhvGGajjL_-NmDIWFSXl5JikNozppQ"
    CREDENTIALS = json.dumps(os.environ.get("GOOGLE_SHEETS_CREDENTIALS"))

    def __str__(self):
        return self.value
