# social/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('perfil/<int:usuario_id>/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),

]
