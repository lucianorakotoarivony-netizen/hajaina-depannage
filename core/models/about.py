from django.db import models
from .mixins import SingletonModel
from filer.fields.image import FilerImageField

class About(SingletonModel):
    title=models.CharField("Titre", max_length=200, default="A propos")
    content=models.TextField("Contenu")
    image=FilerImageField(blank=True, null=True, on_delete=models.SET_NULL, 
                           related_name="about_image" )

    class Meta(SingletonModel.Meta):
        verbose_name="Page A propos"
        verbose_name_plural="Page A propos"
    
    def __str__(self) -> str:
        return "Configuration A propos"