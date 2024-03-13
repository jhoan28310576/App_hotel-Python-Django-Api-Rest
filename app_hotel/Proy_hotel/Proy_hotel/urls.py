

from gestion.admin import admin_site
from django.urls import  path, include
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin_site.urls),
    path('estadisticas/', include('gestion.urls')),  
    path('mostrar_habitaciones/', include('informacion.urls')),
    path('habitaciones/', include('habitaciones.urls')),
    path('contactanos/', include('contactanos.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)