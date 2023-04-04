from django.db import models

# Create your models here.
class CursoChirho(models.Model):
    nombre_chirho=models.CharField(max_length=50)
    comision_chirho=models.IntegerField()

class EstudianteChirho(models.Model):
    nombre_chirho=models.CharField(max_length=50)
    apellido_chirho=models.CharField(max_length=50)
    email_chirho=models.EmailField()

class ProfesorChirho(models.Model):
    nombre_chirho=models.CharField(max_length=50)
    apellido_chirho=models.CharField(max_length=50)
    email_chirho=models.EmailField()  
    prefesion_chirho=models.CharField(max_length=50)

class EntregableChirho(models.Model):
    nombre_chirho=models.CharField(max_length=50)
    fecha_chirho=models.DateField()
    entregado_chirho=models.BooleanField()
