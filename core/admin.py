from django.contrib import admin
from django.http.request import HttpRequest
from .models import Home, Service, About, Contact, Hardware, Software

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    #On empêche d'ajouter ou supprimer (toujours une seule ligne)
    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    #Champs à afficher
    fieldsets=(
        ('Informations générales', {
            'fields': ('site_name', 'tech_name', 'tagline')
        }),
        ('Apparence', {
            'fields': ('primary_color',),
            'classes': ('collapse',),  # Plié par défaut
        }),
    )
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    #On empêche d'ajouter ou supprimer (toujours une seule ligne)
    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    fieldsets = (
        ('Coordonnées', {
            'fields': ('phone', 'email')
        }),
    )
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=["name","price","order","is_active"]
    list_editable=["order", "is_active"]
    list_filter=["is_active"]
    search_fields=["name","description"]

@admin.register(About)
class AdminABout(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    fieldsets=((None,{
        "fields": ("title","content","image")
    }),)

@admin.register(Software)
class AdminSoftware(admin.ModelAdmin):
    list_display = [ 'name', 'price', 'order', 'version', 'is_active']
    list_editable=["order", "is_active"]
    list_filter = ['is_active', 'version']
    search_fields = ['name']

@admin.register(Hardware)
class AdminHardware(admin.ModelAdmin):
    list_display = [ 'name', 'price', 'order', 'warranty', 'is_active']
    list_editable=["order", "is_active"]
    list_filter = ['is_active', 'warranty']
    search_fields = ['name']