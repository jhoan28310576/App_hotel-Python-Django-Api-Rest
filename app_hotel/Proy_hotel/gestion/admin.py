
# Register your models here.

# jhoan13
#Jh28310576

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from habitaciones.models import Habitacion, Cliente, Reserva, Pago, Servicio, ServicioHabitacion, fotohabitacioninformation
class MyAdminSite(admin.AdminSite):
    site_header = 'Mi sitio de administración'
    site_title = 'Mi sitio de administración'
    index_title = 'Inicio'

    def get_app_list(self, request, for_site_menu=False):
        """
        Devuelve una lista ordenada de aplicaciones y modelos para la página de índice.
        """
        app_dict = self._build_app_dict(request)
        # Ordena las aplicaciones alfabéticamente.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Personaliza el orden de tus modelos aquí.
        order = {'User': 1, 'Group': 2, 'Habitacion': 3, 'Cliente': 4, 'Reserva': 5, 'Pago': 6, 'Servicio': 7, 'ServicioHabitacion': 8, 'fotohabitacioninformation': 9}

        # Ordena los modelos dentro de las aplicaciones.
        for app in app_list:
            app['models'].sort(key=lambda x: order.get(x['object_name'], 0))

        return app_list
    
class HabitacionAdmin(admin.ModelAdmin):
    list_display =('numero', 'tipo', 'ocupada',)
    search_fields =('numero', 'tipo', 'ocupada',)
    list_filter =('numero',)
    
class ClienteAdmin(admin.ModelAdmin):
    list_display =('nombre', 'email',)
    search_fields =('nombre', 'email',) 
    list_filter=('nombre',)
    
class ReservaAdmin(admin.ModelAdmin):
    list_display =('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin',)
    search_fields =('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin',)
    list_filter=('fecha_inicio',)
    
class PagoAdmin(admin.ModelAdmin):
    list_display =('reserva', 'cantidad', 'fecha')
    search_fields =('reserva', 'cantidad', 'fecha')
    list_filter=('fecha',)
    
class ServicioAdmin(admin.ModelAdmin):
    list_display =('nombre', 'descripcion',)
    search_fields =('nombre', 'descripcion',)
    list_filter=('nombre',)
    
class ServicioHabitacionAdmin(admin.ModelAdmin):
    list_display =('habitacion', 'servicio', 'fecha',)
    search_fields =('habitacion', 'servicio', 'fecha',)
    list_filter=('fecha',)

class fotohabitacioninformationAdmin(admin.ModelAdmin):
    list_display =('title','image', 'descripcion',)
    search_fields =('image', 'descripcion', )
    list_filter=('descripcion',)

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Habitacion, HabitacionAdmin)
admin_site.register(Cliente, ClienteAdmin)
admin_site.register(Reserva, ReservaAdmin)
admin_site.register(Pago, PagoAdmin)
admin_site.register(Servicio, ServicioAdmin)
admin_site.register(ServicioHabitacion, ServicioHabitacionAdmin)
admin_site.register(fotohabitacioninformation, fotohabitacioninformationAdmin)