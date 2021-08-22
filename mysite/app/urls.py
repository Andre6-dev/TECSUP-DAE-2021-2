from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path("", views.index, name="index"),
    path('suma/<int:firstnumber>/<int:secondnumber>/', views.sumar, 
    name='sumar'),
    path('resta/<int:firstnumber>/<int:secondnumber>/', views.restar, 
    name='restar'),
    path('multiplicacion/<int:firstnumber>/<int:secondnumber>/', views.multiplicar, 
    name='multiplicar'),
    path('division/<int:firstnumber>/<int:secondnumber>/', views.dividir, 
    name='dividir'),
    
]