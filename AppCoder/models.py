from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return f"curso: {self.nombre}, camada:{self.camada}"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Profesor: {self.nombre}, {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entreg = models.DateField()
    entregado = models.BooleanField()
