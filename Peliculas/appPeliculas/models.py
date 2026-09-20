from django.db import models

# Create your models here.



class genero (models.Model):
    gen_nombre = models.CharField(max_length=60, unique=True)
    
    def __str__(self) -> str:
        return self.gen_nombre
 

class tipo (models.Model):
    tip_nombre = models.CharField(max_length=60, unique=True)
    
    
    def __str__(self) -> str:
        return self.tip_nombre    

class peliculas (models.Model):
    pel_codigo = models.CharField(max_length=10, unique=True)
    pel_titulo = models.CharField(max_length=80)
    pel_protagonista = models.CharField(max_length=80)
    pel_duracion = models.IntegerField()
    pel_sinopsis = models.CharField(max_length=2000)
    pel_foto = models.ImageField(upload_to=f"fotos/", null=True, blank=True)
    pel_genero = models.ForeignKey(genero, on_delete=models.PROTECT)
    pel_tipo = models.ForeignKey(tipo, on_delete=models.PROTECT)
    pel_visto = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.pel_titulo
    