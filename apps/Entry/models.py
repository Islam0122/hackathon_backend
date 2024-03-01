from django.db import models

from apps.basemodel.models import BaseModel


class Entry(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Записи справочника'
        ordering = ['-id']