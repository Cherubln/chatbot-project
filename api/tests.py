from django.test import TestCase
from .models import UserData
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch


class GoogleSheetsDataTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('utils.google_sheets.get_google_sheet_data')
    def test_import_data_from_sheet(self, mock_get_google_sheet_data):
        mock_get_google_sheet_data.return_value = [
            {
                "name": "John Doe",
                "age": 30,
                "gender": "Male",
                "height": 180,
                "weight": 75,
                "smoking_status": "non-smoker",
                "exercise_frequency": 3,
                "diet_quality": "Good",
                "medical_history": "None"
            }
        ]

        response = self.client.get(reverse('import_data_from_sheet'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(UserData.objects.filter(name='John Doe').exists())
