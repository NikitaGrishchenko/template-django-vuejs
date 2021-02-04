from .common import BACKEND_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BACKEND_DIR / "db.sqlite3",
    }
}


SECRET_KEY = "7ih8a1tz&91#kd9k0y^!bjdlp(5lu))%h0rf*v-=8olgs@1!q3"

ALLOWED_HOSTS = ["*"]

