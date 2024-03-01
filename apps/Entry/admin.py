from django.contrib import admin
from django.utils.html import format_html

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ['title', 'text']
    list_filter = ['title']

    def image_(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.photo.url))

    image_.admin_order_field = 'Изображение'

    fieldsets = [
        ('Основная информация', {
            'fields': ['image_', 'photo', 'title', 'text']
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),

    ]
    readonly_fields = ['image_', 'created_at', 'updated_at']
