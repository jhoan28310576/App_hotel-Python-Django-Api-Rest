from django.urls import path
from gestion import views

urlpatterns = [
    path('estadisticas/', views.obtener_estadisticas_habitaciones, name='estadisticas_habitaciones'),
    
]
