from django.db import models

class ActiveManager(models.Manager):
    """
    Ce manager filtre automatiquement les objets pour ne garder 
    que ceux marqués comme actifs et les trie par leur champ 'order'.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True).order_by('order')