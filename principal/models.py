from django.db import models

# Create your models here.


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    imagen = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    generos = [
        ('Caballero', 'Caballero'),
        ('Dama', 'Dama'),
        ('Unisex', 'Unisex'),
        ('Niños', 'Niños'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    imagen = models.URLField(blank=True, null=True)
    genero = models.CharField(max_length=100, choices=generos)
    marca = models.ForeignKey(Marca, on_delete=models.SET("NULL"), blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

