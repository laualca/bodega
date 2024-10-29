from django.shortcuts import render, HttpResponse

from inventario.models import Inventario


# Create your views here.

def inicio(request):
    return render(request, 'BodegaInventarioApp/inicio.html')

def mantenimiento(request):
    return render(request, 'BodegaInventarioApp/mantenimiento.html')

def transacciones(request):
    return render(request, 'BodegaInventarioApp/transacciones.html')

def inventario(request):
    
    inventario = Inventario.objects.all()
    #return render(request, 'BodegaInventarioApp/inventario.html')
    return render(request, 'BodegaInventarioApp/inventario.html', {"inventario":inventario})
def reportes(request):
    return render(request, 'BodegaInventarioApp/reportes.html')