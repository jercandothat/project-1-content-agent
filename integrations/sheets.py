import gspread
from oauth2client.service_account import ServiceAccountCredentials

def append_to_sheet(sheet_id: str, values: list, creds_file: str):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id).sheet1
    sheet.append_row(values)
    print(f"[SUCCESS] Appended row to Google Sheet {sheet_id}")