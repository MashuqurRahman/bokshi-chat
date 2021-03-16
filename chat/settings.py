# chat/settings.py
"""Base Settings."""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ABC1234'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Apps
    'core',
    # 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'channels',
    'crispy_forms',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'corsheaders',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'chat.wsgi.application'
ASGI_APPLICATION = 'chat.asgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'bokshi_chat',
#         'USER': 'shahid',
#         'PASSWORD': 'password',
#         'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'bokshi_chat'),
        'USER': os.environ.get('DJANGO_DB_USER', 'root'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': os.environ.get('DJANGO_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DJAGNO_DB_PORT', '3306'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# {
#     'NAME':
#  'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# },
# {
#     'NAME':
# 'django.contrib.auth.password_validation.MinimumLengthValidator',
# },
# {
#     'NAME':
# 'django.contrib.auth.password_validation.CommonPasswordValidator',
# },
# {
#     'NAME':
# 'django.contrib.auth.password_validation.NumericPasswordValidator',
# },

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # new
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

MESSAGES_TO_LOAD = 15


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/


ADMIN_MEDIA_PREFIX = '/static/admin/'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'

ALLOWED_HOSTS = ['*']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
CRISPY_TEMPLATE_PACK = 'bootstrap4'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1

STATIC_URL = '/static/'
# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'staticfiles')
# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

MEDIA_URL = '/media/'
# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'mediafiles')


CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000',
)

# development setup
if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

    # deployment setup

if not DEBUG:
    ALLOWED_HOSTS = ['*']
