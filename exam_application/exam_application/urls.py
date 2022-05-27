"""
 Този urls.py е основният за нашият проект, той се намира в конфигурационната папка, 
 която също носи името на проекта.
 Тази конфигурация ще определи нашия главни url-и.
 Тоест всеки нашите app-ве ще има top level url , с който ще започва.
 например  всичко, което започва с /admin ще присвои линковете на admin.site.urls
 това прави връзката между view-то и контролерите от админ пакета на джанго, което ще ни осигури 
 напълно функцониращ администраторски панел.

 localhost:8000/account
 ще ни даде всички urlpatterns от accounts/urls.py , което от своя страна ще ни даде много 'пътища 
 свързани към контролерите на accounts, които се намират в accounts/views.py

"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from accounts.views import profile

"""
  urlpatterns e масив от пътища, които от своя страна ще извикат функции, обработващи и връщанни данни по някакъв начин
  може да бъде html,json или обикновен http

"""
urlpatterns = [
    path('', profile, name = 'langin' ),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # при localhost:8000/accounts/ включи всички exam_application accounts/urls.py
    path('modules/', include('modules.urls')),
    path('exams/', include('exams.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
