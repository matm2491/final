from django.db import models
# importo los modelos de la base de datos de postgres ya creados buscandolos con el comando (manage.py inspectdb)

class TinDependencias(models.Model):
    descripcion = models.CharField(max_length=150, blank=True, null=True)
   


    def __str__(self):
        return "%s" % (self.descripcion)

    

    class Meta:
        managed = False
        db_table = 'tin_dependencias'


class TinUsuarios(models.Model):  
    dependencia = models.ForeignKey(TinDependencias, models.DO_NOTHING, blank=True, null=True)  
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    
    descripcion_cargo = models.CharField(max_length=120, blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido = models.CharField(max_length=30, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    tlf_extension = models.CharField(max_length=20, blank=True, null=True)


    

    #para que me muestre primer nombre y priemr apellido en el admin de django

    def __str__(self):
        return "%s %s" % (self.primer_nombre, self.primer_apellido)

    

    #referencia a la misma clase de modelo

    class Meta:
        managed = False
        db_table = 'tin_usuarios'




# Create your models here.


   

