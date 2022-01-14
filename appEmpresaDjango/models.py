from django.db import models
from django.db.models.base import Model

# Create your models here.

class Departamento(models.Model):
    # No es necesario crear un campo para la primary key, Django creara automaticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self) -> str:
        return f"id={self.id}, nombre={self.nombre}, telefono={self.telefono}"


class Habilidad(models.Model):
    # No es necesario crear un campo para la primary key, Django creara automaticamente un IntegerField.
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"id={self.id}, nombre={self.nombre}"


class Empleado(models.Model):
    # Campo para la relacion one-to-many
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)    

    def __str__(self) -> str:
        return f"id={self.id}, nombre={self.nombre}, fecha_nacimiento={self.fecha_nacimiento}, antiguedad={self.antiguedad}"