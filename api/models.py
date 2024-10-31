from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default='Not specified')
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    smoking_status = models.CharField(max_length=10, default='non-smoker')
    exercise_frequency = models.IntegerField(default=0)
    diet_quality = models.CharField(max_length=10, default='Unknown')
    medical_history = models.TextField(default='None')
    timestamp = models.DateTimeField(auto_now_add=True)
    insurance_risk = models.IntegerField(default=0)
    diabetes_risk = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
