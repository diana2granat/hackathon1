from config_copy import api_key
from googleapiclient.discovery import build


# sheet_id = '1rCkekA1zHOJH2Jzi0Uo27RaG8EFHfiw2WqOAYTFkPuk'  # ID of the Google Sheet you want to access
# range_name = 'Sheet1!A5:C'  # Range of cells to retrieve data from (e.g., A1:B10)
# service = build('sheets', 'v4', developerKey=api_key) # Create a service object for interacting with the Google Sheets API
# result = service.spreadsheets().values().get( # Call the Sheets API to get values from the specified range
#     spreadsheetId=sheet_id,
#     range=range_name
# ).execute()

# # Extract values from the response
# values = result.get('values', [])

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


# user = [1,"Jeremy", "Gross","email@email.com","0556667777","Jerusalem","2024-03-21 16:30:47.731897+02"]
# def loop_values():
#     matching_opportunities = []
#     for value in values:
#         if value[1] == user[5]:
#             matching_opportunities.append(value)
#     if matching_opportunities:
#         print("We found some matches in your city:")
#         for opportunity in matching_opportunities:
#             print(opportunity)
#     else:
#         print("No matches found in your city.")

# loop_values()