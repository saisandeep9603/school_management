from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',notice_form,name='notice_form'),
]