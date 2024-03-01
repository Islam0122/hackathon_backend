from django.db import models

from apps.basemodel.models import BaseModel


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='subcategories', verbose_name='Родительская категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Entry(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='entries', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись справочника'
        verbose_name_plural = 'Записи справочника'
        ordering = ['-id']
