import os
from pathlib import Path

from .environment import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent
BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = os.path.join(BACKEND_DIR, "apps")
PROJECT_DIR = os.path.dirname(BACKEND_DIR)
FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")
STATIC_DIR = os.path.join(FRONTEND_DIR, "static")
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, "templates")
DIST_DIR = os.path.join(STATIC_DIR, "dist")
WEBPACK_STATS_FILE = os.path.join(DIST_DIR, "webpack-stats.json")
PUBLIC_MEDIA_DIR = os.path.join(STATIC_DIR, "media")
APP_TEMPLATE = os.path.join(APPS_DIR, "base", "management", "template.zip")
ENV_FILE = os.path.join(PROJECT_DIR, ".env")

# Nginx
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
PUBLIC_MEDIA_DIR = os.path.join(PUBLIC_DIR, "media")
PUBLIC_STATIC_DIR = os.path.join(PUBLIC_DIR, "static")

# Admin
ADMIN_USERNAME = env("ADMIN_USERNAME", default=None)
ADMIN_PASSWORD = env("ADMIN_PASSWORD", default=None)
ADMIN_EMAIL = env("ADMIN_EMAIL", default=None)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "webpack_loader",
    "rest_framework",
    "widget_tweaks",
    "apps.base",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"




AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Auth

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# webpack

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "dist/",
        "STATS_FILE": WEBPACK_STATS_FILE,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = "/static/"
STATIC_ROOT = PUBLIC_STATIC_DIR
STATICFILES_DIRS = [STATIC_DIR, DIST_DIR]

MEDIA_ROOT = PUBLIC_MEDIA_DIR
MEDIA_URL = "/media/"

# REST API
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
