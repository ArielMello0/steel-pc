from django.db import models

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
    nombre=models.CharField(max_length=50)
    num_blog=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.num_blog)




