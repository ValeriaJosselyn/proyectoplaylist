from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    foto_url = models.URLField(max_length=500, blank=True, null=True)
    album = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=50, default="Pop")
    letra = models.TextField(blank=True, null=True)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=80)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.cancion.titulo}"