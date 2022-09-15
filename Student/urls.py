from django.urls import path
from . import views
urlpatterns = [
        path('courseMaterial', views.courseMaterial, name='courseMaterial'),





]