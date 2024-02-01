from django.urls import path
from . import views

urlpatterns = [
    
    path('informacion/', views.informacion, name='informacion_'),
]