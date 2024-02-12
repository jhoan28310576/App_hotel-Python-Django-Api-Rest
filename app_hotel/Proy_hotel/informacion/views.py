from django.shortcuts import render
from habitaciones.models import fotohabitacioninformation 
# Create your views here.

def mostrar_habitaciones(request):
    try:
       fotos = fotohabitacioninformation.objects.filter(id__in=[1, 2 , 3,])
    except fotohabitacioninformation.DoesNotExist:
         raise Http404("La foto no existe")
    return render(request, 'informacion.html', {'fotoss': fotos})