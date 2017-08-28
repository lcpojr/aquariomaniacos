from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aquariomaniacos',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': ''
    }
}

INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1')
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
