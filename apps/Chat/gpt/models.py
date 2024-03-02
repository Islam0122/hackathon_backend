from django.db import models
from django.contrib.auth.models import User

from apps.Chat.Patient.models import Patient


# class ChatRecord(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     input_message = models.TextField()
#     gpt3_response = models.TextField()
#
#     def __str__(self):
#         return f"{self.user.username}"


class ChatRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.TextField(verbose_name='Введенный запрос')
    ai_response = models.TextField(verbose_name='Ответ искусственного интеллекта')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')

    def str(self):
        return f"Запрос чата №{self.id} ({self.timestamp})"

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
