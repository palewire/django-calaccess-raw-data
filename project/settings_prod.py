DEBUG = False
DEVELOPMENT, PRODUCTION = False, True
DEBUG_TOOLBAR = False
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',
        'USER': '', 
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60 * 30,
    }
}
STATIC_URL = ''
