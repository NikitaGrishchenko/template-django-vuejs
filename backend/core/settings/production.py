SECRET_KEY = "7ih8a1tz&91#kd9k0y^!bjdlp(5lu))%h0rf*v-=8olgs@1!q3"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER' : 'user_name',
        'PASSWORD' : 'password',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

