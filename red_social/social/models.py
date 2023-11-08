# social/models.py

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Publicación de {self.autor}'

class Conexion(models.Model):
    seguidor = models.ForeignKey(Usuario, related_name='seguidor', on_delete=models.CASCADE)
    siguiendo = models.ForeignKey(Usuario, related_name='siguiendo', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seguidor} sigue a {self.siguiendo}'
