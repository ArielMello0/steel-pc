from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suscriptor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+ self.apellido
    
class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido


class Blog(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=80)
    cuerpo= models.CharField(max_length=5000)
    autor= models.CharField(max_length=50)
    fecha= models.DateField ()
    imagen= models.ImageField(upload_to='media', null=True, blank=True)


    def __str__(self):
        return self.titulo, self.autor , self.fecha , self.imagen

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares')

