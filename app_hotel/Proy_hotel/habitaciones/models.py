from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Habitacion(models.Model):
    numero = models.IntegerField()
    TIPO_CHOICES = [
        ('baja', 'Gama Baja'),
        ('media', 'Gama Media'),
        ('alta', 'Gama Alta'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ocupada = models.BooleanField(default=False)

    
    class Meta:
        db_table = 'Habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        
    
    def __str__(self):
        return str(self.numero)
    
    def get_absolute_url(self):
        return reverse("Habitacion", kwargs={"pk": self.pk})
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    
    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return str(self.nombre)
    
    def get_absolute_url(self):
        return reverse("Cliente", kwargs={"pk": self.pk})

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pagada = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        return str(self.cliente)
    
    def get_absolute_url(self):
        return reverse("Reserva", kwargs={"pk": self.pk})
    

class Pago(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateField()
    
    class Meta:
        db_table = 'Pago'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
    
    def __str__(self):
        return str(self.reserva)

    def get_absolute_url(self):
        return reverse("Pago", kwargs={"pk": self.pk})
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=190)
    descripcion = models.TextField()
    
    class Meta:
        db_table = 'Servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
    def __str__(self):
        return str(self.nombre)
    
    def get_absolute_url(self):
        return reverse("Servicio", kwargs={"pk": self.pk})
    
class ServicioHabitacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    
    class Meta:
        db_table = 'ServicioHabitacion'
        verbose_name = 'ServicioHabitacion'
        verbose_name_plural = 'ServicioHabitaciones'
            
    def __str__(self):
        return str(self.habitacion)
    
    def get_absolute_url(self):
        return reverse("ServicioHabitacion", kwargs={"pk": self.pk})
    
class fotohabitacioninformation(models.Model):
    title = models.CharField(max_length=50, default='Descripción por defecto')#  estas do como la iamgen y el descripcion van para que el la informacion se vea que habitacion hay para reservar
    image = models.ImageField(upload_to='gestion_img')#  estas do como la iamgen y el descripcion van para que el la informacion se vea que habitacion hay para reservar
    descripcion = RichTextField(default='Descripción por defecto')      #  estas do como la iamgen y el descripcion van para que el la informacion se vea que habitacion hay para reservar
    
    class Meta:
        db_table = 'fotohabitacioninformation'
        verbose_name = 'fotohabitacioninformation'
        verbose_name_plural = 'fotohabitacioninformationes'
        
    def __str__(self):
        return self.descripcion
        
    def get_absolute_url(self):
            return reverse("fotohabitacioninformation", kwargs={"pk": self.pk})
        
        
        