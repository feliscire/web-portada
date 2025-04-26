from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title