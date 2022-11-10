# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'garanti_express',
        'USER': 'postgres',
        'PASSWORD': '1sakura1',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3e#vew4=$(9j0!sy)7+$jse)#2q!ix61n)!znie7c6koctvh(%'