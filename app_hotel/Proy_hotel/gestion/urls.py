from django.urls import path
from gestion import views


urlpatterns = [
    path('estadisticas/', views.obtener_estadisticas_habitaciones, name='estadisticas_habitaciones'),
    path('estadisticas-ocupadas-json/', views.estadisticas_habitaciones_ocupadas_json, name='estadisticas_ocupadas_json'),
]

