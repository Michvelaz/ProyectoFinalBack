from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicacion = models.DateField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
