import json
import os
from enum import Enum


class GitHub(Enum):
    OWNER = 'karbolinivan'
    REPO_DOCS = 'GSPOTtestingdocumentation'
    REPO_TESTS = "GSPOTbackendtest"
    TOKEN = os.environ.get('GITHUB_PARSER')
    # TOKEN = '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'
    SERVICES = ["Games"]
    BRANCH_GH = "gh-pages"

    def __str__(self):
        return self.value


class Sheets(Enum):
    SPREADSHEET_ID = "1s0f-YtiR_4uCymhvGGajjL_-NmDIWFSXl5JikNozppQ"
    # CREDENTIALS = json.dumps(os.environ.get("GOOGLE_SHEETS_CREDENTIALS"))
    CREDENTIALS = {
  "type": "service_account",
  "project_id": "gspotbackend",
  "private_key_id": "649d2548d9d9b6ef8f220cea796e901a7a935d71",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDIpl1vE70jzRiD\n84JKQwpRUqqgk2Yg2fjjw+Pfyr24uZ2kj32GvdojPFzrhYPza6D+eoe+q6JXvD/3\noj8Fa16mDHyDP60Z21AGlt5Y927GvTOb0WfneEa2yzHW79Th31sBemtn8y5RA4MP\nG2TupxSbMGD7+FR5dsKjMGDpv2YNU6fefxuiRto/PW7bgVyYdYeQaEKBNWcFV5LT\nfnxNhnGgRkxCpmvnp3CNusaX6G3jMMzAMm6XW5oRaVAs+ohOKCkMhaUeZbqXlRK9\n8NeaX2xHdKmLAS9/B1yLMpjb++v1x3HnEnmJwXzt8I6eemqQJniJZN+M9Wwz7sso\nPcEFWAWlAgMBAAECggEAKdh2UnDLqJCArR4m/T1ThMfIgXIUIcRLsZacKsNBw2lk\njNoHDAeCm4geedjvvp+i5QehUTzCv+jo70hlO8hbZiZi/k1UmLiiDSnAJ848ilKR\nlYy7zmyJVNx2IbUFUPDvrhR9m2F+NpOUrN0h9NqgA8h4ZXwyA93mdDml8IHD8wGx\ne7gaqi2j6+yWMWjh5RL2Gyt0omNth3Q1ULkcBu7GqYtMUhYdy/TxlZDtCo+//Qv4\njfrGcWMBq65Q1tOObbf4AJUdok6ENmTliWZLE7wfq21/yfaY7BPEQwIvPm+ko5sb\nV2oV6E443MEWglkwwKp1cn7TXTxjmWpzga23LQmjAQKBgQDr+IUOXqiFO2/bvyio\ncQ2Do6duCK0ie5ycvCswQN0Se6ES9HKHxYvSve0T8v183nFG4vCAvfNqh1R22FL7\nTmWGigKTPTPj5Nlh9NV9OjM4m2CqmvAmutGjbI8yme2s23ruJU48b/933XBW5hjR\nt0dqDdRYQY+GzlxwcAwvNQzlAQKBgQDZrlirceeOV5jiZCIjCtc6Mqc9IP2iAjs/\nuI1Gxq87gL4ebNK3XKiisglLnm1MV3Aqbc+r6A4Rn6sUOabziYXjeE52QtUfqwml\npRi0AQKPyVTgwmeF7+/L/p2Db/0sKDmR7jvE2GMRhnIspuD4VPNNRGm6DpS4VLCs\n5Vt+x2xspQKBgQDmErLQ1vRiqxgeXtzqlwgBMOC/hVAiDfoeS82kR6oFKmtbiuHc\nhX0WJj5ws/v58vzpi73JGOusE3UER1lpU//jVM679vGQIwLc4pYBemyUpdJzpYu/\nh2l9eQyJ3tGBN6I9bjxA60Zf/ZVZ9RF/8L59pixDPPEPFEfHDUikAoqnAQKBgC7W\n+zF5AxB3/OfKECZmMMXPHHlk3e68eC9P8OZn3lD5dO9rDzRxdb/8e0+QOYiR0Arx\nMhyVhGF6b/+cIDaLQwodWxTLcLytuxevnM8u4HQ8KE1sx4XkiT7l/NLJiDq2NR0X\nnDjRLxAYU/0Ts5j7/paDwBRPCuVXI+UwPS3cj5IZAoGBAOpZW2kepvgOJEiodPpH\ntwwqAQm78DmDqQB+7wv06pSK7GVkdcyu+u3e53p17rGmJl6IC1OHFi3J43QXu4JK\nTih8mOrfdOR5fIsk2RfTOD+HaneIKVRslMV6BuRejB80j2Mb0xo/9th0id0Owf+J\n4H95J9NasaLGOZinFqPAecIz\n-----END PRIVATE KEY-----\n",
  "client_email": "service@gspotbackend.iam.gserviceaccount.com",
  "client_id": "102291888417474781516",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service%40gspotbackend.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


    def __str__(self):
        return self.value
