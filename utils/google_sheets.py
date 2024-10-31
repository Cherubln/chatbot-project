import os
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings

# Configure logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Reference the path to the service account file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(
    __file__), '../config/service-account.json')
# Replace with your actual Google Sheet ID
SHEET_ID = settings.SHEET_ID
RANGE_NAME = 'Sheet1'  # Update range as per your sheet structure


def get_google_sheet_data():
    try:
        # Authenticate using service account
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE
        )
        service = build('sheets', 'v4', credentials=credentials)

        # Retrieve data from Google Sheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
        rows = result.get('values', [])

        # Process and return the data
        headers = rows[0] if rows else []
        data = [dict(zip(headers, row)) for row in rows[1:]]
        return data

    except FileNotFoundError:
        logging.error(
            "Service account file not found. Please check the file path.")
    except HttpError as e:
        logging.error(
            f"HTTP error occurred while accessing Google Sheets API: {e}")
    except KeyError:
        logging.error(
            "Error accessing data from the response. Check the sheet range and headers.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    # Return an empty list if an error occurs
    return []
