from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    # Pour order les caterogies en les classant par les plus recentes aux plus anciennes

    class Meta:
        ordering = ['-date_added']

# Ceci permet d'eviter que dans admin, on mette objet1.. quanad on ajoute une ctegorie
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_added']

    # Ceci permet d'eviter que dans admin, on mette objet1.. quanad on ajoute un produit
    def __str__(self) -> str:
        return self.title
    
class Commande(models.Model):
    items = models.CharField(max_length=400) # Recuperent les infos de l'utilisateur
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['date_commande']



   
