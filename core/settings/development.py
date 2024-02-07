from pathlib import Path
from decouple import config

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Секретный ключ проекта
SECRET_KEY = config('SECRET_KEY')

# Разрешенные хосты (укажите конкретные хосты)
ALLOWED_HOSTS = ['*']
# Уровень отладки
DEBUG = config('DEBUG', default=False, cast=bool)

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}