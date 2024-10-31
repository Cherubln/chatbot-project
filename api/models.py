from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bmi = models.FloatField()
    lifestyle_score = models.IntegerField()
    insurance_risk = models.IntegerField()
    diabetes_risk = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
