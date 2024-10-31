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

#### Approach

- This solution is implemented using Django as the backend framework, with the following core functionalities:

#### 1. Data Retrieval:

- A get_google_sheet_data function retrieves data from a Google Sheet using the Google Sheets API.
  Error handling is incorporated to manage any potential issues, including authentication, connectivity, and API errors.

#### 2. Error Handling & Logging:

- Comprehensive error handling in both the Google Sheets data retrieval and the API submission functions.
  Logging of each error type to ensure any issues can be quickly diagnosed and resolved.

#### 3. Storage & Retrieval:

- Data is stored in a database with the UserProfile model, making it easy to access historical data for any user.

### Folder Structure

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
