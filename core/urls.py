# core/urls.py
from django.urls import path
from .views import view_configs, create_config

urlpatterns = [
    path('', view_configs, name='view_configs'),
    path('configs/create/', create_config, name='create_config'),
]
