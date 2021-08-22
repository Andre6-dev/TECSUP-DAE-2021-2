from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Desde la vista de app!")

def sumar(request, firstnumber, secondnumber):
    return HttpResponse("La suma de ambos numeros es: " 
    + str(firstnumber + secondnumber))

def restar(request, firstnumber, secondnumber):
    return HttpResponse("La resta de ambos numeros es: " 
    + str(firstnumber - secondnumber))

def multiplicar(request, firstnumber, secondnumber):
    return HttpResponse("La multiplicacion de ambos numeros es: " 
    + str(firstnumber * secondnumber))

def dividir(request, firstnumber, secondnumber):
    return HttpResponse("La division de ambos numeros es: " 
    + str(firstnumber / secondnumber))
