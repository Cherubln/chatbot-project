from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData
from .serializers import UserDataSerializer
from utils.google_sheets import get_google_sheet_data
import random


@api_view(['GET'])
def import_data_from_sheet(request):
    google_sheet_data = get_google_sheet_data()
    created_entries = []

    for entry in google_sheet_data:
        insurance_risk = random.randint(1, 10) + int(entry.get('age', 0)) // 10
        diabetes_risk = random.randint(
            1, 10) + (5 if float(entry.get('bmi', 0)) > 25 else 0)

        user_data = UserData.objects.create(
            name=entry.get('name', ''),
            age=int(entry.get('age', 0)),
            gender=entry.get('gender', ''),
            smoking_status=entry.get('smoking_status', ''),
            diet_quality=entry.get('diet_quality', ''),
            medical_history=entry.get('medical_history', ''),
            height=float(entry.get('height', 0)),
            weight=float(entry.get('weight', 0)),
            exercise_frequency=int(entry.get('exercise_frequency', 0)),
            insurance_risk=insurance_risk,
            diabetes_risk=diabetes_risk
        )

        created_entries.append(UserDataSerializer(user_data).data)

    return Response(created_entries)
