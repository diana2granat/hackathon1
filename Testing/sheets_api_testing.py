from test_config_copy import api_key
from googleapiclient.discovery import build


def get_google_sheet_values():
    sheet_id = '1rCkekA1zHOJH2Jzi0Uo27RaG8EFHfiw2WqOAYTFkPuk'
    range_name = 'Sheet1!A5:C'

    
    service = build('sheets', 'v4', developerKey=api_key) # Create a service object for interacting with the Google Sheets API


    result = service.spreadsheets().values().get( # Call the Sheets API to get values from the specified range
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()

    # Extract values from the response
    values = result.get('values', []) # Extract values from the response
    return values

