from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    hospital_number = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
