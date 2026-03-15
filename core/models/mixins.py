from django.db import models

class SingletonModel(models.Model):
    class Meta:
        abstract=True
    def save(self, *args, **kwargs):
        """Force l'ID à 1 pour garantir un singleton en base"""
        self.pk=1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Empêche la suprresion du singleton"""
        return(0, {})
    
    @classmethod
    def load(cls):
        obj, created=cls.objects.get_or_create(pk=1)
        return obj