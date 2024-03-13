from django.shortcuts import render
from habitaciones.models import Habitacion

def obtener_estadisticas_habitaciones(request):
    # Obtén la cantidad de habitaciones en cada categoría
    gama_baja = Habitacion.objects.filter(tipo='baja').count()
    gama_media = Habitacion.objects.filter(tipo='media').count()
    gama_alta = Habitacion.objects.filter(tipo='alta').count()

    # Pasa los datos a la plantilla
    return render(request, 'estadisticas.html', {
        'gama_baja': gama_baja,
        'gama_media': gama_media,
        'gama_alta': gama_alta,
    })



    
