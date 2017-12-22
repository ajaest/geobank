from core.settings import envconf

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': envconf.BM_DB_NAME,
        'USER': envconf.BM_DB_USER,
        'PASSWORD': envconf.BM_DB_PASSWORD,
        'HOST': envconf.BM_DB_HOST,
        'PORT': envconf.BM_DB_PORT
    }
}
