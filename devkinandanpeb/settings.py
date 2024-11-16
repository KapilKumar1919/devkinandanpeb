import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-89qx)pmxvs@4k&gch)jza4#i=##w@o&+=7e-3p)(u5n-1!zop*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['devkinandanpeb.com', 'www.devkinandanpeb.com', '3.110.55.255', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee',
    'company',
    'country',
    'currency',
]

SITE_ID = 1

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

ROOT_URLCONF = 'devkinandanpeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WSGI_APPLICATION = 'devkinandanpeb.wsgi.application'

ASGI_APPLICATION = 'devkinandanpeb.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'devkinandanpeb.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'devkinandanpeb',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'db',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Email Configs
# EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
# EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
# EMAIL_FROM = config('EMAIL_FROM', default='YK PEB STRUCTURE <admin@no-reply.com>')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='gauravkulshrestha757@gmail.com')  # Use your Gmail account
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='vrlc znbz wqpn icnw')  # Use your Gmail app password
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# This should be a directory that is accessible by Nginx
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Change this path to where you want your collected static files to be

# Additional directories where static files are located (used during development)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # This points to the development static directory
]

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATE_INPUT_FORMATS = ['%d-%m-%Y']
TIME_INPUT_FORMATS = ('%I:%M %p',)

# CORS_ALLOW_ALL_ORIGINS = True
#
# CORS_ORIGIN_WHITELIST = [
#     'http://127.0.0.1:8000',
# ]
#
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:8000",
# ]
