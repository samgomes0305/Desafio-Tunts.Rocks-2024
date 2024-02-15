import os.path
import math
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1uRzubDXnEtrKeFJKW9lpV6YjsnJ2LQnnNtbZ5GF-vzs"
SAMPLE_RANGE_NAME = "engenharia_de_software!A3:H27"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  print("Verifying credentials...")
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    print("Credentials loaded from token.json.")
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
      print("Credentials refreshed.")
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
      print("User authenticated successfully.")
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    print("Calling Google Sheets API...")
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    
    # Get values from the result of the Sheets API call.
    values = result['values']

    add_values_situacao = [
      [],
    ]
    add_values_nota = [
       [],
    ]
    # Iterate through each line (row) of values in the spreadsheet.
    for i, line in enumerate(values):
      # Skip the header (first line) of the spreadsheet.
      if i > 0:
        # Extract relevant data from the current line.
        faltas = int(line[2])
        P1 = int(line[3])
        P2 = int(line[4])
        P3 = int(line[5])
         # Calculate the average (media) of the three grades and normalize it to a scale of 0 to 10.
        media = (P1 + P2 + P3) / 3
        media = media / 10
        # Determine the 'Situacao' and 'Nota para Aprovacao Final' based on the calculated values.
        faltas_mínimas = 60 * 0.25
        if faltas > faltas_mínimas:
            situacao = 'Reprovado por Falta'
            naf = 0
        elif media < 5:
            situacao = 'Reprovado por Nota'
            naf = 0
        elif media < 7:
            situacao = 'Exame Final'
            # Calculate 'Nota para Aprovacao Final' using the given formula and round up to the nearest integer.
            naf = math.ceil((10 - media) * 10)
        else:
            situacao = 'Aprovado'
            naf = 0
        # Append the calculated 'Situacao' and 'Nota para Aprovacao Final' to the respective lists.
        add_values_situacao.append([situacao])
        add_values_nota.append([naf])  
    # Update the spreadsheet with the calculated values for 'Situacao' and 'Nota para Aprovacao Final'.
    print("Updating spreadsheet with calculated values...")
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='G3', valueInputOption='USER_ENTERED', body={'values': add_values_situacao}).execute()
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='H3', valueInputOption='USER_ENTERED', body={'values': add_values_nota}).execute()
    
    print("Execution completed successfully.")
    
  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()