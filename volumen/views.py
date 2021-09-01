import math

from django.shortcuts import render


# Create your views here.


def formulario(request):
    return render(request, 'formulario.html')


def respuestaform(request):
    diametro = request.POST['n1']
    altura = request.POST['n2']
    resultadov = ((float(diametro)/2)**2) * float(altura) * math.pi
    context = {
        'resultado_formula': resultadov,
    }

    return render(request, 'respuestaform.html', context)
