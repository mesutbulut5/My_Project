from __future__ import unicode_literals
from . import views
from django.contrib import admin
from django.urls import path

#Burada tanımladığımız linkleri belirtiyoruz. Ve views.py dosyasındaki fonksuyonları çağırıyoruz. 
urlpatterns = [
    #Burada name ile isimlendirme yapiyoruz ve bunu çagiriyoruz link olarak istedigimiz yerde. 
    path("", views.index, name="anasayfa"),
    path("index", views.index),
    path("category/<slug:slug>",views.blogs_by_category, name="blogs_by_category"),
    path("blogs", views.blogs, name="renkler")
]
