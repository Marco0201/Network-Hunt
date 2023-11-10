"""
Django settings for networkhuntproject project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ['Domain_name']]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "members",
    "jobapps",
    "hitlist",
    'bootstrap4',
    "bootstrap_datepicker_plus",
    'tinymce',
    
    

    # The following apps are required:

    'allauth',

    # the line below to allows for django login by username, etc
    'allauth.account',

    'allauth.socialaccount',

    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.linkedin_oauth2',

    # automatically handles deletion of imagefields and filefields for objects
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "networkhuntproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {

        'APP': {
            'client_id': os.environ['Google_client_id'],
            'secret': os.environ['Google_secret'],
            'key': ''
        }
        
    },

    'github': {

        'APP': {
            'client_id': os.environ['Github_client_id'],
            'secret': os.environ['Github_secret'],
            'key': ''
        }
    },


}

WSGI_APPLICATION = "networkhuntproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }

    'default': {
        'ENGINE': os.environ['dbEngine'],
        'NAME': os.environ['dbName'],
        'USER': os.environ['dbUser'],
        'PASSWORD': os.environ['dbPassword'],
        'HOST': os.environ['dbHost'],
        'PORT': int(os.environ['dbPort']),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/networkhuntproject'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_SIGNUP_REDIRECT_URL = 'account_login'

SOCIALACCOUNT_LOGIN_ON_GET=False
ACCOUNT_EMAIL_VERIFICATION = "none"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_ADAPTER = 'members.adapter.AccountAdapter'

SOCIALACCOUNT_ADAPTER = 'members.adapter.SocialAccountAdapter'


BOOTSTRAP_DATEPICKER_PLUS = {
     "options": {
        "format": "MM/DD/YYYY",
        "showTodayButton": True,
        "showClear": True,
    },
}


TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    # the code below enables image upload but to the database not to the static folder
    # "file_picker_callback": """function (cb, value, meta) {
    #     var input = document.createElement("input");
    #     input.setAttribute("type", "file");
    #     if (meta.filetype == "image") {
    #         input.setAttribute("accept", "image/*");
    #     }
    #     if (meta.filetype == "media") {
    #         input.setAttribute("accept", "video/*");
    #     }

    #     input.onchange = function () {
    #         var file = this.files[0];
    #         var reader = new FileReader();
    #         reader.onload = function () {
    #             var id = "blobid" + (new Date()).getTime();
    #             var blobCache = tinymce.activeEditor.editorUpload.blobCache;
    #             var base64 = reader.result.split(",")[1];
    #             var blobInfo = blobCache.create(id, file, base64);
    #             blobCache.add(blobInfo);
    #             cb(blobInfo.blobUri(), { title: file.name });
    #         };
    #         reader.readAsDataURL(file);
    #     };
    #     input.click();
    # }""",
    # "content_style": "body { font-family:Roboto,Helvetica,Arial,sans-serif; font-size:14px }",
    
}