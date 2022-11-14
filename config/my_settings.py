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

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtpout.secureserver.net"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'diyorbeknever@gmail.com'
# EMAIL_HOST_PASSWORD = 'Qwerty1110'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'diyorbeknever@gmail.com'
EMAIL_HOST_PASSWORD = 'wyrenxcuawvokxyq'
EMAIL_PORT = 465
EMAIL_USE_SSL = True