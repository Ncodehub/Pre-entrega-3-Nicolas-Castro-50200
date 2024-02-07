from django.db import models

# Create your models here.
class Repuestos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class Maquina(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
