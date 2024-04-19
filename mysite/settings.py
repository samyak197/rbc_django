import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load sensitive information from environment variables
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-mvo)v1ha_pmk63fk=*eph*v#g-5_t6je#8a2hi5bmc&(x-f970')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Allowed hosts specified for your deployment domain on Vercel
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '.vercel.app').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # You can keep this, even though you don't use static files
    'rbc',  # Add your application name here
    'background_task',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

# Templating configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database configuration: Use an in-memory database for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # You can use sqlite3 for simplicity
        'NAME': ':memory:',  # Use an in-memory database if you don't want persistence
    }
}

# Password validation configuration
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

# Internationalization configuration
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'  # You can keep this, even though you don't use static files

# Background tasks configuration
BACKGROUND_TASK_RUN_ASYNC = True

# Channels configuration (use a different backend in production if needed)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # Use a different backend in production if needed (e.g., Redis)
    }
}

# CORS settings
CORS_ALLOW_ALL_ORIGINS = False  # More secure approach than allowing all origins
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')

# Additional configurations specific to your project may be added here
