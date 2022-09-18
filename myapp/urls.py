from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about',views.aboutus),
    path('contact',views.contact),
    path('service',views.service),
    path('msg',views.msg)
]
