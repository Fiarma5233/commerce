from django.contrib import admin

from .models import *

# Register your models here.

# Pour ordonner  en table

admin.site.site_header = "E-commerce"
admin.site.site_title = "Digital Solutions"
admin.site.index_title = "Ingenieur Logiciel"


class AdminCategorie(admin.ModelAdmin):
    list_display= ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added', 'image')
    search_fields = ('title',)
    list_editable = ('price', 'category')

class AdminCommande(admin.ModelAdmin):
    list_display = ( 'items' ,'nom', 'tel', 'email', 'address', 'ville', 'pays', 'total', 'date_commande', 'zipcode')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)