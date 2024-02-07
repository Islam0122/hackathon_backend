from django.apps import AppConfig


class BasemodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basemodel'
