from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "localhost,127.0.0.1"
    ).split(",")
    if host.strip()
]


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'app'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=not DEBUG,
    )
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_TZ = True





STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "default": {
        "BACKEND": "app.storage.SupabaseStorage",
        "OPTIONS": {
            "access_key": os.getenv("SUPABASE_S3_ACCESS_KEY"),
            "secret_key": os.getenv("SUPABASE_S3_SECRET_KEY"),
            "bucket_name": "media",
            "endpoint_url": os.getenv("SUPABASE_S3_ENDPOINT"),
            "region_name": os.getenv("SUPABASE_S3_REGION"),
            "default_acl": None,
            "querystring_auth": False,
        },
    },

    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'




JAZZMIN_SETTINGS = {
    "site_title": "AgendaPro",
    "site_header": "AgendaPro",
    "site_brand": " AgendaPro",

    "welcome_sign": "Bem-vindo ao AgendaPro",
    "copyright": "AgendaPro",

    "search_model": [
        "app.Agendamento",
        "app.Servico",
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "app.Agendamento": "fas fa-calendar-check",
        "app.Servico": "fas fa-cut",

        "auth.User": "fas fa-user-shield",
        "auth.Group": "fas fa-users-cog",
    },

    "order_with_respect_to": [
        "app",
        "auth",
    ],

    "custom_css": "admin/css/custom_admin.css",

    "related_modal_active": True,

    "changeform_format": "horizontal_tabs",

    "show_ui_builder": False,
}
