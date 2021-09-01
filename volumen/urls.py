from django.urls import path

from . import views

app_name = 'volumen'

urlpatterns = [
    path('formulario', views.formulario, name='formulario'),
    path('respuestaform', views.respuestaform, name='respuestaform'),
]