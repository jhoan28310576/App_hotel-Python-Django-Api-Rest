from django.shortcuts import render
from django.http import JsonResponse
from habitaciones.models import Reserva, Habitacion, Cliente
from django.db.models import Count

def obtener_estadisticas_habitaciones(request):
    # Obtén la cantidad de habitaciones en cada categoría
    gama_baja = Habitacion.objects.filter(tipo='baja', ocupada=False).count()
    gama_media = Habitacion.objects.filter(tipo='media', ocupada=False).count()
    gama_alta = Habitacion.objects.filter(tipo='alta', ocupada=False).count()

    # Pasa los datos a la plantilla
    return render(request, 'estadisticas.html', {
        'gama_baja': gama_baja,
        'gama_media': gama_media,
        'gama_alta': gama_alta,
    })

def estadisticas_habitaciones_ocupadas_json(request):
    # Asegúrate de que este código se ejecuta correctamente
    gama_baja_ocupada = Habitacion.objects.filter(tipo='baja', ocupada=True).count()
    gama_media_ocupada = Habitacion.objects.filter(tipo='media', ocupada=True).count()
    gama_alta_ocupada = Habitacion.objects.filter(tipo='alta', ocupada=True).count()

    data = {
        'gamaBajaOcupada': gama_baja_ocupada,
        'gamaMediaOcupada': gama_media_ocupada,
        'gamaAltaOcupada': gama_alta_ocupada,
    }
    return JsonResponse(data)

from django.http import JsonResponse

def obtener_estadisticas_reservas_ajax(request):
    reservas_pagadas = Reserva.objects.filter(pagada=True).count()
    reservas_no_pagadas = Reserva.objects.filter(pagada=False).count()
    clientes_con_reserva = Cliente.objects.filter(reserva__isnull=False).distinct().count()

    data = {
        'reservas_pagadas': reservas_pagadas,
        'reservas_no_pagadas': reservas_no_pagadas,
        'clientes_con_reserva': clientes_con_reserva,
    }

    return JsonResponse(data)
    
