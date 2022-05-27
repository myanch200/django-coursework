"""
django изпозва Model View Template  (MVT) pattern-а, за да 
осигури разделение на отговорностите в нашето приложение.
Също така конвенцията е логиката да бъде разделена на множество app-ове 
или под приложения като всяко едно от тях да се грижи за малък на брой функционалности на цялостното приложение
====Model=====
Model-ът представлява 1 таблица от нашата база с данни, с помощта на Object Object–relational mapping  ORM
той преобразува тези таблици в python класове, върху които ние можем да изпикваме функции за обработването, 
селекцирането и манипулирането на тези данни.



View-та са всички файлове съдържащи логиката за презентирането на данните от моделите ни, той е връзката между моделът и нашият front-end
без значение далие html json или нещо друго. В много други рамки за разработване (frameworks) това се нарича Controller
и съответно  pattern-a се нарича Model View Controller.
===== Tamplates =====

Tamplate е нашия презентационнен слой на приложението неговата задача е определи как информацията ще бъде представена на клиента или по скоро структурата на този начин
Тук основно пишем html във който 'вграждаме' python код за да изпълним някаква логика 
като да вземем всеки елемент от колекция и да направим ред във таблица за него.
Понякога обаче този слой не ни е нужен,защото сме прибегнали до javascript библиотека или рамка , която да се грижи за тази част
В този случай view-то ще върне някакъв лесен за обработване формат,който не съдържа много освен информацията ,която ни е нужна.
Най- често срещаните формати са json и XML.


==== URLS
Има и четвърти слой, който макар и не вписан във pattern-a използван от Django  играе огромна роля.
urls.py съдържат пътищата към нашият сайт и в зависимост от пътя зададен от request-a извиква специфична функция.
Той е връзката между темплейтите и view-тата.

===== SETTINGS =====
 В този файл се съдържа цялата конфигурация на нашият проект
 неща като каква база данни, къде да django да намери статичните файлове като 
 css и javascript.
 Всички middleware, както и всички под приложания на django.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q%b1b+dgas&%jre4=@*w=e!)69y!_hp@ii=--1_7la@wqwtn2b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my apps
    'accounts.apps.AccountsConfig',
    'exams.apps.ExamsConfig',
    'modules.apps.ModulesConfig',
    'pages.apps.PagesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exam_application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        
    },
]

WSGI_APPLICATION = 'exam_application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
