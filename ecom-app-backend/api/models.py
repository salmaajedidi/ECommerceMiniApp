from django.db import models

# Create your models here.
class Product(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix = models.FloatField()
    stock = models.IntegerField() 

    def __str__(self):
        return self.nom