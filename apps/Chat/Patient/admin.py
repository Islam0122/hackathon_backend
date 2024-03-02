from django.contrib import admin
from .models import  Patient
from apps.Chat.gpt.models import ChatRequest


class ChatRequestInline(admin.TabularInline):
    model = ChatRequest
    extra = 0  # Number of empty forms to display
    can_add = False


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'age', 'height', 'weight')
    search_fields = ('full_name',)  # Assuming user is related to the User model
    inlines = [ChatRequestInline]

    fieldsets = (
        ('Общая информация', {
            'fields': ('full_name', 'gender', 'age', 'height', 'weight'),
        }),
        ('Чаты', {
            'fields': ('chat_requests',),
        }),
    )

    readonly_fields = ('chat_requests',)

    def chat_requests(self, obj):
        chat_requests = obj.chatrequest_set.all()
        if chat_requests:
            return '\n'.join(
                [f"ID: {chat.id}\n"
                 f",Запрос: {chat.user_input}\n"
                 f", Ответ ИИ: {chat.ai_response}\n"
                 f", Время: {chat.timestamp}" for
                 chat in chat_requests])
        else:
            return 'Нет чатов для этого пациента.'

    chat_requests.short_description = 'Чаты'


admin.site.register(Patient, PatientAdmin)