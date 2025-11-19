import gspread
from google.oauth2.service_account import Credentials

# Scopes are used to define the specific operations or accesses you want to have for certain files
# when using the Google API
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("fbref-football-data-sheets-creds.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1Qy_gscrEgy4_msbws4-Mm5ztXuR1bEepxBVlJoq8Egw"
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)
print(values_list)