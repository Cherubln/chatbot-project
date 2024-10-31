# Chatbot Data Integration & API Synchronization

## Project Overview

This project showcases data handling, API communication, and backend functionality through a practical data flow and backend synchronization task. The solution retrieves user demographic and lifestyle data from a Google Sheet, processes it, and sends it to a mock backend API. The backend then generates mock insurance and diabetes risk scores, which are stored for future retrieval. Error handling and logging are implemented throughout the project to ensure robustness and easy debugging.

## Table of Contents

- [Project Overview](#background)
- [Approach](#background)
- [Folder Structure](#background)
- [Setup Instructions](#background)
- [How to Run the Application](#background)
- [Testing](#background)
- [Project Goals & Alignment](#background)

<hr>

### Approach

- This solution is implemented using Django as the backend framework, with the following core functionalities:

**1. Data Retrieval:**

- A `get_google_sheet_data` function retrieves data from a Google Sheet using the Google Sheets API.
  Error handling is incorporated to manage any potential issues, including authentication, connectivity, and API errors.

**2. Error Handling & Logging:**

- Comprehensive error handling in both the Google Sheets data retrieval and the API submission functions.
  Logging of each error type to ensure any issues can be quickly diagnosed and resolved.

**3. Storage & Retrieval:**

- Data is stored in a database with the UserProfile model, making it easy to access historical data for any user.

## Folder Structure

```
project_root/
├── api/
│   ├── __init__.py
│   ├── urls.py                 # API endpoints routing
│   ├── views.py                # Core logic for handling requests
│   ├── tests.py                # Unit tests for API functionality
├── utils/
│   ├── __init__.py
│   ├── google_sheets.py        # Data retrieval from Google Sheets API
├── chatbot_project/
│   ├── __init__.py
│   ├── settings.py             # Django project settings
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt            # List of required Python packages
└── README.md                   # Project Description
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Django
- Google Sheets API and Google Cloud Service Account
- Required Python packages are listed in requirements.txt

### Steps

**1. Clone the Repository:**

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

**2. Set Up a Google Cloud Service Account:**

Go to the Google Cloud Console.

- Enable the Google Sheets API.
- Create a service account and download the JSON credentials file.
- Place the JSON file in the project directory (recommended path: project_root/service_account.json).
- Add the service account email to your Google Sheet with Viewer permissions.

**3. Environment Variables:**

- In `myproject/settings.py`, set up environment variables for sensitive data, including the Google Sheet ID and path to the service account JSON file.

**4. Install Required Packages:**

```bash
pip install -r requirements.txt
```

**5. Run Database Migrations:**

```bash
python manage.py migrate
```

## How to Run the Application

**1. Start the Django Development Server:**

```bash
Copy code
python manage.py runserver
```

**2. Access the API Endpoint:**

- The API endpoint for data retreival is located at `http://127.0.0.1:8000/api/import_data_from_sheet/.`
  Use a tool like Postman or curl to send a request or simply access this URL for automatic data fetching.

## Testing

**1. Run Unit Tests:**

- The `api/tests.py` file contains unit tests for the core functionality.
- To run all tests, execute:

```bash
python manage.py test api
```

**2. Verify Successful Test Output:**

- All tests should pass, indicating that the data retrieval, and error handling functions are working correctly.

## Project Goals & Alignment

**1. Retrieve Data from Google Sheets:**

- The `get_google_sheet_data` function retrieves user data from Google Sheets, catching errors and logging them for debugging.

**2. Data Storage:**

- The data and calculated scores are saved in the database via the `UserData` model, enabling future access.

**3. Error Handling:**

- Comprehensive error handling for Google Sheets retrieval, API communication, and database storage, ensuring the application is robust and reliable.

**4. Documentation & Testing:**

- This `README.md` provides setup and usage instructions.
  Unit tests confirm the reliability of key functionalities, allowing for continuous integration and development.
