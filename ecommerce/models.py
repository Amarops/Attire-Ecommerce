from django.db import models

# Create your models here.
class Producto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    precio = models.IntegerField()
    descuento = models.IntegerField(null=True, blank=True)
    valoracion = models.IntegerField()
    categoria = models.CharField(max_length=50, verbose_name='Categoría')
    descripcion = models.TextField(max_length=2500, verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "categoria: " + self.categoria + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using = None, keep_parents = False):
        try:
            self.imagen.storage.delete(self.imagen.name)
            super().delete()
        except:
            super().delete()
        


class Blog (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=90, verbose_name='Título')
    usuario = models.CharField(max_length=50, verbose_name='Usuario')
    texto = models.TextField(verbose_name='Texto', max_length=2500)
    imagen = models.ImageField(upload_to='ecommerce/static/images', verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Autor: " + self.usuario 
        return fila