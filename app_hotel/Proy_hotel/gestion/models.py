
from django.db import models

# Create your models here.


class Habitacion(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=200)
    ocupada = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.numero)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.nombre)

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
        return str(self.cliente)

class Pago(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateField()
    
    def __str__(self):
        return str(self.reserva)

class Servicio(models.Model):
    nombre = models.CharField(max_length=190)
    descripcion = models.TextField()
    
    def __str__(self):
        return str(self.nombre)
    
class ServicioHabitacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    
    def __str__(self):
        return str(self.habitacion)
