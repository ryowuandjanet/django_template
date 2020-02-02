from .base import *

# 將base.py DEBUG 和 ALLOWED_HOSTS 移到這裡(需修改)
DEBUG = config('DEBUG',cast=bool)
ALLOWED_HOSTS = ['ip-address','www.your-website.com']

# 將base.py AUTH_PASSWORD_VALIDATORS 移到這裡(不做修改)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 將 DATABASES 移到這裡(需修改上線時的設定)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

# 新增 STRIPE_PUBLIC_KEY 及 STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')