from django.urls import path

from . import views

app_name = 'ejercicios'

urlpatterns = [
    path('operaciones', views.operaciones, name='operaciones'),
    path('respuestaope', views.respuestaope, name='respuestaope'),
]
