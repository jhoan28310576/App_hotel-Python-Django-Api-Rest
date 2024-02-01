from django.shortcuts import render

# Create your views here.
def habitaciones(request):
    return render(request, 'habitaciones.html')