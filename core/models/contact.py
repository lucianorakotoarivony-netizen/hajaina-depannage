from django.db import models
from django.core.validators import RegexValidator
from .mixins import SingletonModel

class Contact(SingletonModel):
    """Les contacts"""
    MESSAGE="Le numéro doit contenir exactement 10 chiffres (0355555555)"
    phone_validator=RegexValidator(regex=r'^0\d{9}$', message=MESSAGE)
    phone=models.CharField(
        "Téléphone", 
        max_length=10, 
        help_text=MESSAGE, 
        validators=[phone_validator], 
        default="0123456789")
    email=models.EmailField("Email", default="contact@depanneur-pc.com")

    def __str__(self) -> str:
        return "Configuration des contacts"
    
    class Meta(SingletonModel.Meta):
        verbose_name="Contact"
        verbose_name_plural="Contacts"
    