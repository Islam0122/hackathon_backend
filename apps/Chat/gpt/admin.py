from django.contrib import admin
from .models import *

class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'timestamp', 'user')
    search_fields = ('patient__full_name', 'user__username')  # Assuming user is related to the User model

    list_filter = ('patient__full_name', 'user')

    fieldsets = (
        ('Пациент', {
            'fields': ['patient__full_name', 'patient__gender', 'patient__age', 'patient__height', 'patient__weight']
        }),
        ('Чат', {
            'fields': ('user_input', 'ai_response', 'timestamp'),
        }),
        ('Пользователь', {
            'fields': ('user',)
        }),
    )


admin.site.register(ChatRequest, ChatRequestAdmin)