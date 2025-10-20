from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.CharField(max_length=100)
    
    # En lugar de ForeignKey, usa campos normales:
    id_categoria = models.IntegerField()  
    id_proveedor = models.IntegerField()  
    
    def __str__(self):
        return f'{self.id_producto} - {self.nombre}'