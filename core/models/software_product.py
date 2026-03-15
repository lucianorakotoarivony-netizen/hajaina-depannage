from django.db import models
from .product import Product
from filer.fields.image import FilerImageField

class Software(Product):
    version=models.CharField("Version", max_length=200, blank=True)
    icon=models.CharField("Icône", max_length=50,blank=True,help_text="Emoji ou classe CSS")
    image=FilerImageField(blank=True, null=True, on_delete=models.SET_NULL, 
                           related_name="software_image" )
    class Meta(Product.Meta):
        verbose_name="Logiciel"
        verbose_name_plural="Logiciels"
        db_table="software_products"