from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from .viewssonu import*
from django.conf.urls.static import static
urlpatterns=[
    path('',home),
    path('about',about),
    path('tracking',tracking),
    path('hp',hp),
    path('jk',jk),
    path('uk',uk),
    path('contact',contact),
    path('booking',bookingg),
    path('test1',test1),
    path('payment',payment),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)