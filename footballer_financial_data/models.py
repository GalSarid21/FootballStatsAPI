from django.db import models

class FootballerFinancialData(models.Model):
    full_name = models.CharField(max_length=50, unique=True)
    net_worth = models.PositiveBigIntegerField()
    currency = models.CharField(max_length=5)
    nationality = models.CharField(max_length=20)
    other_professions = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now_add=True)
