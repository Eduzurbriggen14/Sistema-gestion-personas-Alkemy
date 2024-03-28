from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE )

    class Meta:
        ordering = ('pk',)

    def __str__(self) -> str:
        return f"{self.nombre}--Precio: ${self.precio}"



