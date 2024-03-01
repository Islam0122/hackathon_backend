from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'id')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')

    def image_(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.photo.url))

    image_.admin_order_field = 'Изображение'

    fieldsets = [
        ('Основная информация', {
            'fields': ['image_', 'photo', 'title','category', 'text']
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),

    ]
    readonly_fields = ['image_', 'created_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    search_fields = ('name',)


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
