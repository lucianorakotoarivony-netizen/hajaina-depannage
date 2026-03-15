from django.db import models
from .mixins import SingletonModel

class Home(SingletonModel):
    "Information générales sur la page d'accueil"
    site_name= models.CharField("Nom du site", max_length=200, default="Hajaina dépannage PC")
    tech_name=models.CharField("Nom du technicien", max_length=200, default="Hajaina dépannage PC")
    tagline=models.CharField("Slogan", max_length=200, blank=True, default="Informaticien de confiance", help_text="Ex: Votre dépanneur de confiance")
    availability=models.TextField("Disponibilité", default="Du lundi au vendredi, de 9h à 17h")
    primary_color = models.CharField("Couleur principale", max_length=7, 
                                     default="#007bff", help_text="Ex: #007bff")
    
    class Meta(SingletonModel.Meta):
        verbose_name="Accueil"
        verbose_name_plural="Accueil"

    def __str__(self) -> str:
        return "Configuration de l'Accueil"