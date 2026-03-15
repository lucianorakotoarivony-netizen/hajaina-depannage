from django.db import models
from django.core.validators import MinValueValidator
from .manager import ActiveManager
class Product(models.Model):
    name=models.CharField("Nom du produit", max_length=200)
    price=models.IntegerField("Prix", validators=[MinValueValidator(0)])
    description=models.TextField("Description", blank=True)
    is_active=models.BooleanField("Actif", default=True)
    order=models.IntegerField("Ordre d'affichage", default=0, validators=[MinValueValidator(0)])
    objects=models.Manager()
    available=ActiveManager()
    
    class Meta:
        abstract=True
        ordering=["order", "name"]

    def __str__(self) -> str:
        return self.name