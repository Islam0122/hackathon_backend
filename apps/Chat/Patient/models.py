from django.db import models
from apps.basemodel.models import BaseModel


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужчина'),
        ('F', 'Женщина'),
    ]

    full_name = models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    age = models.IntegerField(verbose_name='Возраст')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Рост')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Вес')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return self.full_name