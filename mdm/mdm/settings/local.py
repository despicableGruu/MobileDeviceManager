from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = 'brianmuse33@gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASE_USER = get_secret("DATABASE_USER")
DATABASE_PASSWORD = get_secret("DATABASE_PASSWORD")
DATABASE_PORT = get_secret("DATABASE_PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MDM_DB',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': DATABASE_PORT,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static", "static"),)
