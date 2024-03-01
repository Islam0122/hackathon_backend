import os
from pathlib import Path
from decouple import config as env

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Секретный ключ проекта
SECRET_KEY = env('SECRET_KEY')

# Режим отладки
DEBUG = env('DEBUG', default=True)

# Разрешенные хосты
ALLOWED_HOSTS = ['*']

# Подключенные приложения
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'phonenumber_field',
    'apps.basemodel',
    'apps.Patient',
    'apps.Entry',
]

# Промежуточные программы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'core.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Язык и временная зона
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Приложение WSGI
WSGI_APPLICATION = 'core.wsgi.application'

# Статика и медиафайлы
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath("static")
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("media")

# Настройки электронной почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Условный импорт настроек для окружений
if DEBUG:
    from .development import *
else:
    from .production import *

# Импорт настроек для админ-панели Jazzmin
from .jazzmin import JAZZMIN_SETTINGS

CORS_ORIGIN_ALLOW_ALL = True