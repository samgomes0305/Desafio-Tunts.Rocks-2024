### Overview
This Python script demonstrates the basic usage of the Google Sheets API to interact with a specific spreadsheet. The application fetches values from the specified range in the spreadsheet, performs calculations, and updates the spreadsheet with the results.

### Prerequisites
Before running the application, ensure you have the following:
Python installed (version 3.6 or higher)
Required Python packages installed: `os`, `math`, `google.auth.transport.requests`, `google.oauth2.credentials`, `google_auth_oauthlib.flow`, `googleapiclient.discovery`, `googleapiclient.errors`

```pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client```

## Getting Started
1. Clone this repository:

```git clone https://github.com/samgomes0305/Desafio-Tunts.Rocks-2024.git```

2. Navigate to the project directory:

```Desafio-Tunts.Rocks-2024```

3. Run the script:

```main.py```

4. Follow the on-screen instructions to authenticate and authorize the application.

## Important Notes
### Token File (token.json): This file stores the user's access and refresh tokens. If it doesn't exist, the application will guide you through the authentication flow to generate it.

### Sample Spreadsheet Information:

Spreadsheet ID: 1uRzubDXnEtrKeFJKW9lpV6YjsnJ2LQnnNtbZ5GF-vzs

Range: engenharia_de_software!A3:H27

## Output
The script will output information about the authentication process, fetching values, and updating the spreadsheet. In case of any errors, it will display relevant error messages.

Feel free to customize and enhance the script as needed for your specific use case.
