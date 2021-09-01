from django.shortcuts import render


# Create your views here.


def operaciones(request):
    return render(request, 'operaciones.html')


def respuestaope(request):
    a = request.POST['firstnumber']
    b = request.POST['secondnumber']
    c = request.POST['operation']
    suma = int(a) + int(b)
    resta = int(a) - int(b)
    multiplicacion = int(a) * int(b)
    division = int(a) / int(b)
    context = {
        'a': a,
        'b': b,
        'name_operacion': c,
        'resultado_suma': suma,
        'resultado_resta': resta,
        'resultado_multiplicacion': multiplicacion,
        'resultado_division': division,
    }

    return render(request, 'respuestaope.html', context)
