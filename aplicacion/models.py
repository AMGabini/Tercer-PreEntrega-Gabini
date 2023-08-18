from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre
