from django.contrib import admin
from django.urls import path
from calcapp import views

urlpatterns = [
    path('calc/',views.calc),
]
