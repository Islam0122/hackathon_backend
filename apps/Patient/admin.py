from django.contrib import admin

from apps.Patient.models import Patient


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Имя и Фамилия', {'fields': ['full_name']}),
        ('Персональная информация', {'fields': ['gender', 'age']}),
        ('Физические параметры', {'fields': ['height', 'weight']}),
    ]

    list_display = ('full_name', 'gender', 'age', 'height', 'weight')
    search_fields = ['full_name']


admin.site.register(Patient, PatientAdmin)
