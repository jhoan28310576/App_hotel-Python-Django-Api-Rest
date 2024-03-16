from django.urls import path
from gestion import views


urlpatterns = [
    path('estadisticas/', views.obtener_estadisticas_habitaciones, name='estadisticas_habitaciones'),
    path('estadisticas-ocupadas-json/', views.estadisticas_habitaciones_ocupadas_json, name='estadisticas_ocupadas_json'),
    path('obtener_estadisticas_reservas_ajax/', views.obtener_estadisticas_reservas_ajax, name='estadisticas_reservas'),
]

